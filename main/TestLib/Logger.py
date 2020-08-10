class Logger():
    def __init__(self): return

    @staticmethod
    def printArgs(output_string, *args):
        first_arg = True
        for arg in args:
            if first_arg:
                first_arg = False
            else:
                output_string += ', '
            output_string += str(arg)
        return output_string

    @staticmethod
    def info(*args):
        output_string = 'Log Info <= '
        output_string = Logger.printArgs(output_string, *args)
        print(output_string)

    @staticmethod
    def warning(*args):
        output_string = 'Log Warn <= '
        output_string = Logger.printArgs(output_string, *args)
        print(output_string)

    @staticmethod
    def error(*args):
        output_string = 'Log Error <= '
        output_string = Logger.printArgs(output_string, *args)
        print(output_string)
        raise Exception

    @staticmethod
    def test(assertion, *args):
        if not assertion:
            Logger.error(*args)

    @staticmethod
    def fatal(*args):
        output_string = 'Log Fatal <= '
        output_string = Logger.printArgs(output_string, *args)
        print(output_string)
        raise Exception


LOG = Logger()

if __name__ == '__main__':
    LOG.info('Dude', 1)
    LOG.warning('Man', {})
    try:
        LOG.error('Uh oh')
    except:
        print('Error causes exception')

