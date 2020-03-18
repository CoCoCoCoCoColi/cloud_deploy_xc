#!/usr/bin/python3
# coding: utf-8

import simplejson
import subprocess
import sys


def main():
    f=open(sys.argv[1],'r')
    for line in f:
        target = line.replace("\n","")
        print("\n")
        print(target)
        print("\n")
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        }
        cmd = ["/root/xray_craw/crawlergo", "-c", "/tmp/chrome-linux/chrome-linux/chrome",
               "-o", "json", "-m","3000000","-t","20","--push-to-proxy","http://127.0.0.1:6767/","--custom-headers", simplejson.dumps(headers), target]
        rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = rsp.communicate()
        # print(output)
        try:
            result = simplejson.loads(output.decode().split("--[Mission Complete]--")[1])
            req_list = result["req_list"]
            for each in req_list:
                print(each)
        except KeyboardInterrupt:
            sys.exit()
        except Exception:
            continue


if __name__ == '__main__':
    main()
