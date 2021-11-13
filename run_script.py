import os
import datetime
import time
from argparse import ArgumentParser

alg_config = '--config={alg}'
env_config = '--env-config={env}'
map_config = 'with env_args.map_name={map}'
comment_config = '--comment={comment}'

output_folder = './output'
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-c', '--comment', type=str, help='any comment you want to add', default='')
    parser.add_argument('-e', '--env', type=str, help='decide which environment to run', default='sc2')
    parser.add_argument('-m', '--map', nargs='+', help='decide maps to run if choose sc2 env', default=['MMM2'])
    parser.add_argument('-a', '--alg', nargs='+', help='decide algorithms to run', default=['oda_limited_comm'])
    parser.add_argument('-s', '--seeds', nargs='+', help='specify given seeds', default=[])
    parser.add_argument('-r', '--repeat', type=int, help='repeat n times for a given algorithm', default=1)
    parser.add_argument('-o', '--others', nargs='+', help='other configs', default=[])

    args = parser.parse_args()
    
    if str(args.env).startswith('sc2'):
        for map_name in args.map:
            for alg_name in args.alg:
                for i in range(args.repeat):
                    name = '{}_{}'.format(alg_name, args.comment) if len(args.comment) > 0 else alg_name
                    log_name = '{time}-{alg}-{map}.out'.format(
                        alg=name, 
                        map=map_name, 
                        time=datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
                    )
                    command = 'nohup python src/main.py {} {} {} {} {} > {} 2>&1 &'.format(
                        comment_config.format(comment=args.comment), 
                        alg_config.format(alg=alg_name), 
                        env_config.format(env=args.env), 
                        map_config.format(map=map_name), 
                        ' '.join(args.others),
                        os.path.join(output_folder, log_name)
                    )
                    os.system(command)
                    if map_name == args.map[-1] and alg_name == args.alg[-1] and i == args.repeat - 1:
                        pass
                    else:
                        time.sleep(10)
    else:
        for alg_name in args.alg:
            for i in range(args.repeat):
                name = '{}_{}'.format(alg_name, args.comment) if len(args.comment) > 0 else alg_name
                log_name = '{time}-{alg}-{env}.out'.format(
                    alg=name, 
                    env=args.env, 
                    time=datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
                )
                command = 'nohup python src/main.py {} {} {} {} > {} 2>&1 &'.format(
                    comment_config.format(comment=args.comment),
                    alg_config.format(alg=alg_name), 
                    env_config.format(env=args.env), 
                    ('with ' + ' '.join(args.others)) if len(args.others) > 0 else '',
                    os.path.join(output_folder, log_name)
                )
                os.system(command)
                if alg_name == args.alg[-1] and i == args.repeat - 1:
                    pass
                else:
                    time.sleep(10)
