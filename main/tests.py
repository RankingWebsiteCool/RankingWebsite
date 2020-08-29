
if __name__ == "__main__":
    import sys
    sys.path[0] = 'D:/Websites/RankingWebsiteCool'

    from main.TestLib.TestCommon import *

    from main.TestLib.Movies.UrlTests import *
    from main.TestLib.Movies.DatabaseCallTests import *

    local_functions = locals().copy()
    runAllTests(local_functions)
