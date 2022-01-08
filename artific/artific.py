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

        # adding rectangle
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


class InsertionSort:
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
        for i in range(1, self.n):
            key = self.array[0][i]
            j = i-1
            while j >= 0 and key < self.array[0][j] :
                    self.array[0][j + 1] = self.array[0][j]
                    j -= 1
                    self.iter += 1
                    self.create_gif(i, j+1, is_swap=True)
            self.array[0][j + 1] = key

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

        # adding rectangle
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

class HeapSort:
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

    def heapify(self, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and self.array[0][largest] < self.array[0][l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < n and self.array[0][largest] < self.array[0][r]:
            largest = r

        # Change root, if needed
        if largest != i:
            self.array[0][i], self.array[0][largest] = self.array[0][largest], self.array[0][i]  # swap
            self.create_gif(i, largest, is_swap=True)
            # Heapify the root.
            self.heapify( n, largest)
            self.iter+=1

    # The main function to sort an array of given size


    def sort(self):
        n = len(self.array[0])

        # Build a maxheap.
        for i in range(n//2 - 1, -1, -1):
            self.heapify(n, i)

        # One by one extract elements
        for i in range(n-1, 0, -1):
            self.array[0][i], self.array[0][0] = self.array[0][0], self.array[0][i]  # swap
            self.heapify(i, 0)
            
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

        # adding rectangle
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

class BinarySearch:
    def __init__(self, array, value):
        
        assert sorted(array) == array, 'Input array is not sorted!'
        
        self.value = value

        self.n = len(array)
        self.array = array
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

    def search(self, value):
        valueExist = 'not found'
        start = 0
        end = len(self.array)-1
        middle = 0

        while(start<=end):
            middle = int((start+end)/2)
            self.create_gif(middle)  
            if self.array[middle] == value:
                self.create_gif(middle, isFound=True)
                valueExist = middle
                break
            else:
                if self.array[middle]>value:
                    end = middle - 1
                else: 
                    start = middle + 1

        if not os.path.exists('gifs/'):
            os.mkdir('gifs/')
        imageio.mimsave(f'{self.save_dir}/binary_search_{self.iter}.gif', self._ims, fps=self.fps)

        self.saved_gif_path = f'{self.save_dir}/binary_search_{self.iter}.gif'
        self._ims = []
        return valueExist

    def __str__(self) -> str:
        val = self.search(value=self.value)
        if val == 'not found':
            return "Not Found"
        else:
            return str(val)

    def visualize(self):
        import base64
        from IPython import display
        with open(self.saved_gif_path, 'rb') as fd:
            b64 = base64.b64encode(fd.read()).decode('ascii')
        return display.HTML(f'<img src="data:image/gif;base64,{b64}" />')

    def create_gif(self, column_index_left_box, row_index_left_box=0,
                   isFound=False):

        if self.n % self.max_array_len == 0:
            _gif_array = np.reshape(np.array(self.array).reshape(1, self.n), (-1, self.max_array_len))
            row_index_left_box = int(column_index_left_box / self.max_array_len)
            column_index_left_box = column_index_left_box % self.max_array_len
        else:
            _gif_array = np.array(self.array).reshape(1, self.n)
        
        self.input_shape = (len(_gif_array), len(_gif_array[0]))

        scale = 0.8
        figsize = (self.input_shape[1] * scale, self.input_shape[0] * scale)
        fig, ax = plt.subplots(figsize=figsize)
        ax = sb.heatmap(_gif_array, square=True, cbar=False, xticklabels=False, yticklabels=False, annot=True,
                        cmap="cool", linewidths=4)

        # adding rectangle
        if isFound:
            ax.add_patch(Rectangle((column_index_left_box, row_index_left_box), 1, 1, fill=False,
                                   edgecolor=self.rectangle_color_2, lw=4))
        else:
            ax.add_patch(Rectangle((column_index_left_box, row_index_left_box), 1, 1, fill=False,
                                   edgecolor=self.rectangle_color_1, lw=4))

        # create and save gif
        if not os.path.exists('temp/'):
            os.mkdir('temp/')

        img_loc = 'temp/' + 'temp_image_{:d}'.format(self.iter + 1) + '.png'

        plt.savefig(img_loc, bbox_inches='tight', dpi=self.dpi)
        self._ims.append(imageio.imread(img_loc))
        os.remove(img_loc)

        plt.close()


class LinearSearch:
    def __init__(self, array, value):
        
        self.value = value

        self.n = len(array)
        self.array = array
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

    def search(self, value):
        valueExist = 'not found'
        for i in range(len(self.array)):
            self.create_gif(i)  
            if self.array[i] == value:
                valueExist = i
                self.create_gif(i, isFound=True) 
                break 
        if not os.path.exists('gifs/'):
            os.mkdir('gifs/')
        imageio.mimsave(f'{self.save_dir}/binary_search_{self.iter}.gif', self._ims, fps=self.fps)

        self.saved_gif_path = f'{self.save_dir}/binary_search_{self.iter}.gif'
        self._ims = []
        return valueExist

    def __str__(self) -> str:
        val = self.search(value=self.value)
        if val == 'not found':
            return "Not Found"
        else:
            return str(val)

    def visualize(self):
        import base64
        from IPython import display
        with open(self.saved_gif_path, 'rb') as fd:
            b64 = base64.b64encode(fd.read()).decode('ascii')
        return display.HTML(f'<img src="data:image/gif;base64,{b64}" />')

    def create_gif(self, column_index_left_box, row_index_left_box=0,
                   isFound=False):

        if self.n % self.max_array_len == 0:
            _gif_array = np.reshape(np.array(self.array).reshape(1, self.n), (-1, self.max_array_len))
            row_index_left_box = int(column_index_left_box / self.max_array_len)
            column_index_left_box = column_index_left_box % self.max_array_len
        else:
            _gif_array = np.array(self.array).reshape(1, self.n)
        
        self.input_shape = (len(_gif_array), len(_gif_array[0]))

        scale = 0.8
        figsize = (self.input_shape[1] * scale, self.input_shape[0] * scale)
        fig, ax = plt.subplots(figsize=figsize)
        ax = sb.heatmap(_gif_array, square=True, cbar=False, xticklabels=False, yticklabels=False, annot=True,
                        cmap="cool", linewidths=4)

        # adding rectangle
        if isFound:
            ax.add_patch(Rectangle((column_index_left_box, row_index_left_box), 1, 1, fill=False,
                                   edgecolor=self.rectangle_color_2, lw=4))
        else:
            ax.add_patch(Rectangle((column_index_left_box, row_index_left_box), 1, 1, fill=False,
                                   edgecolor=self.rectangle_color_1, lw=4))

        # create and save gif
        if not os.path.exists('temp/'):
            os.mkdir('temp/')

        img_loc = 'temp/' + 'temp_image_{:d}'.format(self.iter + 1) + '.png'

        plt.savefig(img_loc, bbox_inches='tight', dpi=self.dpi)
        self._ims.append(imageio.imread(img_loc))
        os.remove(img_loc)

        plt.close()