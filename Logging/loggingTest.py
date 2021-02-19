import logging
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
list1 = [1, 2,3]
logging.debug(f'This message should go to the log file,{list1}')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


# test2

# import logging
# logFormatter = logging.Formatter("%(asctime)s   %(message)s")
# rootLogger = logging.getLogger()
# fileName='example'
# fileHandler = logging.FileHandler("test.log")
# fileHandler.setFormatter(logFormatter)
# rootLogger.addHandler(fileHandler)
#
# consoleHandler = logging.StreamHandler()
# consoleHandler.setFormatter(logFormatter)
# rootLogger.addHandler(consoleHandler)
#
# logging.info("I am written to the file")


## reading File https://www.cnblogs.com/nancyzhu/p/8551506.html  || https://www.cnblogs.com/yyds/p/6901864.html
## 按照目前的理解，就是log文件输出以及print可以共存，但是必须只能在一个level
# to add var, we need use f''
