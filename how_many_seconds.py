import re

def main():
    while True:
        # 文字入力
        line = input()

        # 01:23:45 みたいな書式なら
        patternHourMinutesSeconds = re.compile(r'^(\d{1,2}):(\d{1,2}):(\d{1,2})$')

        result = patternHourMinutesSeconds.match(line)
        if result:
            hour = int(result.group(1))
            minutes = int(result.group(2))
            seconds = int(result.group(3))
            total_seconds = 3600*hour + 60*minutes + seconds
            # `&t=4040s` のような形で YouTubeのURLの末尾に打てだぜ（＾～＾）
            print(f'{total_seconds}s')
            continue

        print(f'Pass')

main()
