from azure.core.exceptions import ResourceNotFoundError
from azure.ai.ml import dsl, MLClient, Input, MpiDistribution, load_component
from azure.ai.ml.entities import PipelineJob
from azure.ai.ml.entities import Data
from pathlib import Path

base_dir = str(Path(__file__).parent)


def generate_dsl_pipeline() -> PipelineJob:
    # 1. Load component funcs
    basic_func = load_component(path=base_dir + "/component.yml")
    basic_func_dist = load_component(path=base_dir + "/distribution_component.yml")
    uri_file_input = Input(type="uri_file", path="../../data/sample1.csv")
    uri_folder_input = Input(type="uri_folder", path="../../data")

    # 2. Construct pipeline
    @dsl.pipeline(
        description="The hello world pipeline job with data binding",
        compute="cpu-cluster",
        tags={"owner": "sdkteam", "tag": "tagvalue"},
    )
    def pipeline_with_data_binding(
        job_in_folder,
        job_in_file,
        job_in_number: int = 1,
        job_in_string: str = "hello",
        target_compute: str = "cpu-cluster",
        output_file_name: str = "sample1.csv",
    ):
        job_input_binding = basic_func_dist(
            component_in_string=job_in_string, component_in_number=job_in_number, component_in_folder=job_in_folder
        )
        job_input_binding.distribution = MpiDistribution(process_count_per_instance=1)

        node_output_binding = basic_func(component_in_folder=job_input_binding.outputs.component_out_folder)

    pipeline_obj = pipeline_with_data_binding(job_in_folder=uri_folder_input, job_in_file=uri_file_input)
    return pipeline_obj
