import toml

class ConfigLoader():

    instance = None

    def __new__(cls, fileDir=None):
        if not cls.instance:
            cls.instance = super(ConfigLoader, cls).__new__(cls)
            accountFile = f'{fileDir}/conf/account.toml'
            settingFile = f'{fileDir}/conf/setting.toml'

            cls.instance.accountFile = accountFile
            cls.instance.dictAccount = cls.instance.loadUser();

            cls.instance.settingFile = settingFile
            cls.instance.dictSetting = cls.instance.loadSetting();

            print("#初始化完成")
        return cls.instance

    def loadUser(self):
        with open(self.accountFile, encoding="utf-8") as f:
            dic_user = toml.load(f)
        if not dic_user['account']['phoneNumber']:
            phoneNumber = input("# 输入账号")
            password = input("# 输入密码")
            # TODO:检查账户密码的正确性
            dic_user['account']['phoneNumber'] = phoneNumber
            dic_user['account']['password'] = password

            with open(self.accountFile, 'w', encoding="utf-8") as f:
                toml.dump(dic_user, f)

        return dic_user
    def loadSetting(self):
        with open(self.settingFile, encoding="utf-8") as f:
            dic_setting = toml.load(f)
        return dic_setting
