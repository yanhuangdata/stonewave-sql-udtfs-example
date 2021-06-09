from stonewave.sql.udtfs.constants import ParameterDataType as pt


# should change
def supported_signature_list():
    """
    Register function possible parameters type list.
    Stonewave udtf process function using "row" to expression all input parameters,
    so you can handle different parameter list size.
    For example,
    - if you make an "add" function to accept multiple inputs, support all input arguments to
      be added together. Here function processing is same for 2 arguments, 3 arguments or more.
      Now you can append different parameter list for one funtion
    - if you make a "generate_series" function to accept start, end, step three parameters,
      step default is 1, you'd better append one parameter list as:
      [pt.INT, pt.INT, pt.with_default_value(pt.INT, 1)]
    - unsupported for same parameter size but different datatype, because Stonewave system
      support auto cast
    """
    return [
        [pt.INT, pt.STRING, pt.INT],
        [pt.INT, pt.STRING, pt.INT, pt.BOOL],
        [pt.INT, pt.STRING, pt.INT, pt.BOOL, pt.FLOAT],
    ]
