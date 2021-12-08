from AMMMGlobals import AMMMException


class ValidateConfig(object):

    @staticmethod
    def validate(data):
        paramList = [
            "min_iv",
            "max_iv",
            "min_ie",
            "max_ie",
            "min_sv",
            "max_sv",
            "min_se",
            "max_se",
        ]

        for paramName in paramList:
            if paramName not in data.__dict__:
                raise AMMMException(
                    'Parameter (%s) has not been not specified in Configuration' 
                    % str(paramName)
                )

        # vertex values must be integers greater than 1 and edge values must be 
        # integers greater than 0

        min_iv = data.min_iv
        max_iv = data.max_iv
        min_ie = data.min_ie
        max_ie = data.max_ie
        min_sv = data.min_sv
        max_sv = data.max_sv
        min_se = data.min_se
        max_se = data.max_se

        if not isinstance(min_iv, int) or min_iv <= 1:
            raise AMMMException(
                "Value for min_iv is not an integer greater than 1"
            )

        if not isinstance(max_iv, int) or max_iv <= 1:
            raise AMMMException(
                "Value for max_iv is not an integer greater than 1"
            )

        if not isinstance(min_ie, int) or min_ie <= 0:
            raise AMMMException(
                "Value for min_ie is not an integer greater than 1"
            )

        if not isinstance(max_ie, int) or max_ie <= 0:
            raise AMMMException(
                "Value for max_ie is not an integer greater than 1"
            )

        if not isinstance(min_sv, int) or min_sv <= 1:
            raise AMMMException(
                "Value for min_sv is not an integer greater than 1"
            )

        if not isinstance(max_sv, int) or max_sv <= 1:
            raise AMMMException(
                "Value for max_sv is not an integer greater than 1"
            )

        if not isinstance(min_se, int) or min_se <= 0:
            raise AMMMException(
                "Value for min_se is not an integer greater than 0"
            )

        if not isinstance(max_se, int) or max_se <= 0:
            raise AMMMException(
                "Value for max_se is not an integer greater than 0"
            )

        # min values must be lower or equal to their max counterparts

        if not min_iv <= max_iv:
            raise AMMMException(
                "min_iv value must be lower or equal to max_iv"
            )

        if not min_ie <= max_ie:
            raise AMMMException(
                "min_ie value must be lower or equal to max_ie"
            )

        if not min_sv <= max_sv:
            raise AMMMException(
                "min_sv value must be lower or equal to max_sv"
            )

        if not min_se <= max_se:
            raise AMMMException(
                "min_se value must be lower or equal to max_se"
            )
