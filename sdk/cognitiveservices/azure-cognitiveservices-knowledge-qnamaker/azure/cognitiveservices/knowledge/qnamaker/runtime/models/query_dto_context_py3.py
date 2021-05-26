# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .query_context_dto_py3 import QueryContextDTO


class QueryDTOContext(QueryContextDTO):
    """Context object with previous QnA's information.

    :param previous_qna_id: Previous QnA Id - qnaId of the top result.
    :type previous_qna_id: str
    :param previous_user_query: Previous user query.
    :type previous_user_query: str
    """

    _attribute_map = {
        'previous_qna_id': {'key': 'previousQnaId', 'type': 'str'},
        'previous_user_query': {'key': 'previousUserQuery', 'type': 'str'},
    }

    def __init__(self, *, previous_qna_id: str=None, previous_user_query: str=None, **kwargs) -> None:
        super(QueryDTOContext, self).__init__(previous_qna_id=previous_qna_id, previous_user_query=previous_user_query, **kwargs)