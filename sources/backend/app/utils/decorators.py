from drf_spectacular.utils import extend_schema


def extend_res(req=None, res=None, params=None):
  def _decorator(function):
    def _wrap(self, request, *args, **kwargs):
      return function(self, request, *args, **kwargs)
    return extend_schema(
      parameters=[params],
      request=req,
      responses={
        200: res,
        # 400: ErrorSerializer?
      },
    )(_wrap)
  return _decorator