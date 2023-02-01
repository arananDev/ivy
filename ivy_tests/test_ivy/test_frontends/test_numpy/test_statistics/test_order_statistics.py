# global

# local
import ivy_tests.test_ivy.helpers as helpers
import ivy_tests.test_ivy.test_frontends.test_numpy.helpers as np_frontend_helpers
from ivy_tests.test_ivy.helpers import handle_frontend_test

# quantile
@handle_frontend_test(
    fn_tree="numpy.quantile",
    dtype_and_x=helpers.dtype_and_values(
        available_dtypes=helpers.get_dtypes("float", full=True),
        min_num_dims=1,
        max_num_dims=3,
        num_arrays=1,
        shared_dtype=True,
    ),
)
def test_numpy_quantile(
    dtype_and_x,
    frontend,
    test_flags,
    fn_tree,
    on_device,
):
    input_dtypes, xs = dtype_and_x
    np_frontend_helpers.test_frontend_function(
        input_dtypes=input_dtypes,
        frontend=frontend,
        test_flags=test_flags,
        fn_tree=fn_tree,
        on_device=on_device,
        a=xs[0],
        v=xs[1],
    )
