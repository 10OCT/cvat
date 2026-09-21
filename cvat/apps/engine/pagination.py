# Copyright (C) 2019-2022 Intel Corporation
#
# SPDX-License-Identifier: MIT

from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    page_size_query_description = "Number of results to return per page."
    max_page_size = settings.REST_FRAMEWORK["MAX_PAGE_SIZE"]
