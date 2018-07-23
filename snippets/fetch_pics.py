import os
import re
import shutil
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--dataset',
        default='fashion-mnist',
        choices=['fashion-mnist, mnist'],
        type=str
    )

    parser.add_argument(
        '--batch_size',
        default=64,
        type=int,
    )

    parser.add_argument(
        '--epochs',
        default=40,
        type=int,
    )

    parser.add_argument(
        '--gauss',
        default=False,
        dest='gauss',
        action='store_true',
        help='whether the noise in GAN is gaussian'
    )

    return parser.parse_args()


def resave_pics(cmd_args):

    file_names = os.listdir('.')
    temp = []
    for f in file_names:
        if os.path.isdir(f) and (f.startswith('VAE') or f.startswith('GAN')):
            temp.append(f)
    file_names = temp

    pattern = re.compile(r'^(VAE|GAN)_z_(\d+)$')

    root_dir = 'COLLECTED_RESULTS'

    for dir_i in file_names:

        match = pattern.match(dir_i)
        assert match is not None

        model = match.group(1)
        dim = match.group(2)

        target_dir = os.path.join(root_dir, dim)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        if model == 'VAE':
            prefix = model
        elif cmd_args.gauss:
            prefix = '%s_gauss' % model
        else:
            prefix = '%s_unif' % model

        src_file = os.path.join(
            dir_i, 'results',
            '%s_%s_%s_%s' % (model, cmd_args.dataset, cmd_args.batch_size, dim),
            '%s_epoch%03d_test_all_classes.png' % (model, cmd_args.epochs - 1)
        )

        if not os.path.exists(src_file):
            print(src_file)
            continue

        target_file = os.path.join(target_dir, '%s.png' % prefix)

        shutil.copyfile(
            src_file,
            target_file
        )


if __name__ == '__main__':

    args = parse_arguments()
    resave_pics(args)




