import subprocess
import re

user = "kali"

def collect_templates():
    subprocess.call(f"mkdir -p /home/{user}/nuclei-templates/", shell=True)
    templates_repo = ["https://github.com/0x727/ObserverWard_0x727", "https://github.com/0xAwali/Virtual-Host", "https://github.com/0XParthJ/Nuclei-Templates", "https://github.com/1in9e/my-nuclei-templates", "https://github.com/5cr1pt/templates", "https://github.com/adampielak/nuclei-templates", "https://github.com/aels/CVE-2022-37042", "https://github.com/Aituglo/nuclei-templates", "https://github.com/Akokonunes/Private-Nuclei-Templates", "https://github.com/alexrydzak/rydzak-nuclei-templates", "https://github.com/ARPSyndicate/kenzer-templates", "https://github.com/AshiqurEmon/nuclei_templates", "https://github.com/badboy-sft/badboy_17-Nuclei-Templates-Collection", "https://github.com/blazeinfosec/nuclei-templates", "https://github.com/brinhosa/brinhosa-nuclei-templates", "https://github.com/c-sh0/nuclei_templates", "https://github.com/CharanRayudu/Custom-Nuclei-Templates", "https://github.com/ChiaraNRTT96/BountySkill", "https://github.com/clarkvoss/Nuclei-Templates", "https://github.com/d3sca/Nuclei_Templates", "https://github.com/daffainfo/my-nuclei-templates", "https://github.com/dk4trin/templates-nuclei", "https://github.com/ekinsb/Nuclei-Templates", "https://github.com/Elsfa7-110/mynuclei-templates", "https://github.com/esetal/nuclei-bb-templates", "https://github.com/ethicalhackingplayground/erebus-templates", "https://github.com/foulenzer/foulenzer-templates", "https://github.com/geeknik/nuclei-templates-1", "https://github.com/geeknik/the-nuclei-templates", "https://github.com/glyptho/templatesallnuclei", "https://github.com/Harish4948/Nuclei-Templates", "https://github.com/im403/nuclei-temp", "https://github.com/javaongsan/nuclei-templates", "https://github.com/joanbono/nuclei-templates", "https://github.com/justmumu/SpringShell", "https://github.com/kabilan1290/templates", "https://github.com/KeepHowling/all_freaking_nuclei_templates", "https://github.com/kh4sh3i/CVE-2022-23131", "https://github.com/Linuxinet/nuclei-templates", "https://github.com/medbsq/ncl", "https://github.com/meme-lord/Custom-Nuclei-Templates", "https://github.com/MR-pentestGuy/nuclei-templates", "https://github.com/n1f2c3/mytemplates", "https://github.com/NightRang3r/misc_nuclei_templates", "https://github.com/Nithissh0708/Custom-Nuclei-Templates", "https://github.com/NitinYadav00/My-Nuclei-Templates",
                      "https://github.com/notnotnotveg/nuclei-custom-templates", "https://github.com/obreinx/nuceli-templates", "https://github.com/Odayex/Random-Nuclei-Templates", "https://github.com/optiv/mobile-nuclei-templates", "https://github.com/panch0r3d/nuclei-templates", "https://github.com/peanuth8r/Nuclei_Templates", "https://github.com/pentest-dev/Profesional-Nuclei-Templates", "https://github.com/pikpikcu/my-nuclei-templates", "https://github.com/pikpikcu/nuclei-templates", "https://github.com/ping-0day/templates", "https://github.com/praetorian-inc/chariot-launch-nuclei-templates", "https://github.com/projectdiscovery/nuclei-templates", "https://github.com/R-s0n/Custom_Vuln_Scan_Templates", "https://github.com/rafaelcaria/Nuclei-Templates", "https://github.com/rafaelwdornelas/my-nuclei-templates", "https://github.com/rahulkadavil/nuclei-templates", "https://github.com/randomstr1ng/nuclei-sap-templates", "https://github.com/redteambrasil/nuclei-templates", "https://github.com/ree4pwn/my-nuclei-templates", "https://github.com/sadnansakin/my-nuclei-templates", "https://github.com/Saimonkabir/Nuclei-Templates", "https://github.com/Saptak9983/Nuclei-Template", "https://github.com/securitytest3r/nuclei_templates_work", "https://github.com/ShangRui-hash/my-nuclei-templates", "https://github.com/sharathkramadas/k8s-nuclei-templates", "https://github.com/shifa123/detections", "https://github.com/smaranchand/nuclei-templates", "https://github.com/Str1am/my-nuclei-templates", "https://github.com/swisskyrepo/nuclei-templates-wip", "https://github.com/System00-Security/backflow", "https://github.com/tamimhasan404/Open-Source-Nuclei-Templates-Downloader", "https://github.com/test502git/log4j-fuzz-head-poc", "https://github.com/th3r4id/nuclei-templates", "https://github.com/thebrnwal/Content-Injection-Nuclei-Script", "https://github.com/thelabda/nuclei-templates", "https://github.com/themastersunil/Nuclei-TamplatesBackup", "https://github.com/themastersunil/nucleiDB", "https://github.com/toramanemre/apache-solr-log4j-CVE-2021-44228", "https://github.com/toramanemre/log4j-rce-detect-waf-bypass", "https://github.com/trickest/log4j", "https://github.com/wasp76b/nuclei-templates", "https://github.com/wr00t/templates", "https://github.com/yavolo/nuclei-templates", "https://github.com/z3bd/nuclei-templates", "https://github.com/zinminphyo0/KozinTemplates"]
    t = open('/tmp/templates_repo.enforce', 'a')
    for repo in templates_repo:
        save_at = re.findall(
            r'com/[a-zA-Z0-9_-]*/[a-zA-Z0-9_-]*', repo)[0].replace('com/', '')
        t.write(
            f'git clone {repo} /home/{user}/nuclei-templates/{save_at}\n')
    t.close()
    # download all templates
    subprocess.call(
        'interlace -threads 40 -cL /tmp/templates_repo.enforce -t nerrorsec', shell=True)
    # remove files that is not .yaml or .yml
    subprocess.call(
        f"find /home/{user}/nuclei-templates/ -type f -not \(-name '*.yaml' -o -name '*.yml' \) -print -delete", shell=True)
    # remove duplicates
    subprocess.call(
        f"fdupes -r /home/{user}/nuclei-templates/ -d -N", shell=True)
    # remove files that does not match templates syntax
    subprocess.call(f"grep -irlPzv '(?s)^id.*info' /home/{user}/nuclei-templates/ | xargs rm -f", shell=True)
    # validate invalid templates
    subprocess.call(f"nuclei --validate -t /home/{user}/nuclei-templates/ &> /tmp/templates.enforce.invalid", shell=True)
    # remove invalid templates
    subprocess.call(f"grep -iPoh '/home/{user}/nuclei-templates/.*\.(yaml|yml)' /tmp/templates.enforce.invalid | xargs rm -f", shell=True)
    # remove empty directories
    subprocess.call(
        f"find /home/{user}/nuclei-templates/ -empty -type d -delete", shell=True)
collect_templates()
#nerrorsec - NSL
