"""Main module."""

import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import imageio
import os


class BubbleSort:
    def __init__(self, array):
        self.n = len(array)
        self.array = np.array(array).reshape(1, self.n)
        self.iter = 0
        self.input_shape = (1, 1)

        self.fps = 1
        self.dpi = 100
        self.max_array_len = 8
        self.rectangle_color_1 = 'gold'
        self.rectangle_color_2 = 'red'
        self.save_dir = 'gifs/'
        self.custom_save_name = False
        self.save_name = ''
        self.saved_gif_path = ''

        self._ims = []

        self.sort()

    def sort(self):
        assert self.n != 0, 'Array length should be > 0'
        self.iter = 0
        for i in range(self.n):
            for j in range(0, self.n - i - 1):
                self.iter += 1
                if self.array[0][j] > self.array[0][j + 1]:
                    self.array[0][j], self.array[0][j + 1] = self.array[0][j + 1], self.array[0][j]
                    self.create_gif(j, j + 1, is_swap=True)
                else:
                    self.create_gif(j, j + 1, is_swap=False)
        if not os.path.exists('gifs/'):
            os.mkdir('gifs/')
        imageio.mimsave(f'{self.save_dir}/bubble_sort_comparisons_{self.iter}.gif', self._ims, fps=self.fps)

        self.saved_gif_path = f'{self.save_dir}/bubble_sort_comparisons_{self.iter}.gif'
        self._ims = []
        return self.array

    def __str__(self) -> str:
        return str(self.array[0].tolist())

    def visualize(self):
        import base64
        from IPython import display
        with open(self.saved_gif_path, 'rb') as fd:
            b64 = base64.b64encode(fd.read()).decode('ascii')
        return display.HTML(f'<img src="data:image/gif;base64,{b64}" />')

    def create_gif(self, column_index_left_box, column_index_right_box, row_index_left_box=0, row_index_right_box=0,
                   is_swap=False):

        if self.n % self.max_array_len == 0:
            _gif_array = np.reshape(self.array, (-1, self.max_array_len))
            row_index_left_box = int(column_index_left_box / self.max_array_len)
            row_index_right_box = int(column_index_right_box / self.max_array_len)
            column_index_left_box = column_index_left_box % self.max_array_len
            column_index_right_box = column_index_right_box % self.max_array_len
        else:
            _gif_array = self.array

        self.input_shape = (len(_gif_array), len(_gif_array[0]))

        scale = 0.8
        figsize = (self.input_shape[1] * scale, self.input_shape[0] * scale)
        fig, ax = plt.subplots(figsize=figsize)
        ax = sb.heatmap(_gif_array, square=True, cbar=False, xticklabels=False, yticklabels=False, annot=True,
                        cmap="cool", linewidths=4)

        # adding rectange
        if is_swap:
            ax.add_patch(Rectangle((column_index_left_box, row_index_left_box), 1, 1, fill=False,
                                   edgecolor=self.rectangle_color_2, lw=4))
            ax.add_patch(Rectangle((column_index_right_box, row_index_right_box), 1, 1, fill=False,
                                   edgecolor=self.rectangle_color_2, lw=4))
        else:
            ax.add_patch(Rectangle((column_index_left_box, row_index_left_box), 1, 1, fill=False,
                                   edgecolor=self.rectangle_color_1, lw=4))
            ax.add_patch(Rectangle((column_index_right_box, row_index_right_box), 1, 1, fill=False,
                                   edgecolor=self.rectangle_color_1, lw=4))

        # create and save gif
        if not os.path.exists('temp/'):
            os.mkdir('temp/')

        img_loc = 'temp/' + 'temp_image_{:d}'.format(self.iter + 1) + '.png'

        plt.savefig(img_loc, bbox_inches='tight', dpi=self.dpi)
        self._ims.append(imageio.imread(img_loc))
        os.remove(img_loc)

        plt.close()

