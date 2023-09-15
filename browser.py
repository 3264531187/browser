from happy_python import get_exit_code_of_cmd, HappyConfigBase, HappyConfigParser
from datetime import datetime
from pathlib import Path
import json

conf_path = "./config.ini"


class conf(HappyConfigBase):
    def __init__(self):
        super().__init__()

        self.section = 'config'
        self.url = ''
        self.path = ''
        self.node_path = ''
        self.chrom_path = ''
        self.script_path = ''
        self.args = ''


def node_cmd():
    config_path = conf_path
    browser_conf = conf()
    HappyConfigParser.load(config_path, browser_conf)
    current_time = datetime.now()
    url = browser_conf.url
    path = browser_conf.path
    node_path = browser_conf.node_path
    chrom_path = browser_conf.chrom_path
    script_path = browser_conf.script_path
    args = browser_conf.args
    url_access_log_gar_json_path = current_time.strftime("%Y_%m_%d_%H_%M_%S") + '.json'
    url_access_log_jpg_path = current_time.strftime("%Y_%m_%d_%H_%M_%S") + '.jpg'
    url = url
    url_access_log_dir = path + url.replace("http://", "")
    Path(url_access_log_dir).mkdir(exist_ok=True)
    browser_output_path = Path(url_access_log_dir) / url_access_log_gar_json_path
    url_access_log_path = Path(url_access_log_dir) / url_access_log_jpg_path
    node_js_command = '%s %s %s %s %s %s %s' % (
    node_path, script_path, chrom_path, url, browser_output_path, url_access_log_path, args)
    code = get_exit_code_of_cmd(cmd=node_js_command, is_show_error=True, is_show_output=True)
    if code != 0:
        print("erro")
    else:
        # 打开 JSON 文件并加载数据
        json_dic = []
        with open(browser_output_path) as f:
            log_entries = json.load(f)['log']['entries']
            for i in log_entries:

                json_dic.append(i['request']['url'])

        print(json_dic)
        print(len(json_dic))


def main():
    node_cmd()


if __name__ == "__main__":
    main()
