import datetime, os
WORKING_DIR = os.path.abspath(os.path.dirname(__file__))
_config = configparser.ConfigParser()
_config.read(f'{WORKING_DIR}/config.ini')
DEBUGGING = _config['DEBUGGING']['debug_bool']
log = ''


class BugLogger:
    """
    Helper class to debug code while running. Can be turned
    off in the config file by setting 'debug_bool' to False
    """

    @staticmethod
    def bug_log_initialization():
        """
        Check for log directory and file for debugging
        :return:
        """
        if not os.path.exists(f"{WORKING_DIR}{_config['DEBUGGING']['debug_path']}"):
            os.makedirs(f"{WORKING_DIR}{_config['DEBUGGING']['debug_path']}")
        return f"{WORKING_DIR}{_config['DEBUGGING']['debug_path']}{_config['DEBUGGING']['debug_file']}"

    @staticmethod
    def bug_log(msg):
        """
        Call this function to debug code
        To call in application -> BugLogger.bug_log('txt {}'.format(variable))
        :return:
        """
        global DEBUGGING, log
        log += str(datetime.datetime.now()) + ': ' + msg + '\n'
        if DEBUGGING:
            print(str(datetime.datetime.now()) + ': ' + msg)

    @staticmethod
    def bug_log_termination(file):
        """
        Write and close debugging file!
        :param file:
        :return:
        """
        _df = open(file, 'w+')
        _df.write(log)
        _df.close()
