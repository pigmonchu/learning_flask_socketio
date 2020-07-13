from add2numbers.operations.views import Index
from . import operations

add_view = Index.as_view('add')
operations.add_url_rule(
    '/api/v1.0/add',
    view_func=add_view,
    methods=['POST']
)


