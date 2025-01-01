{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "957940af-cd34-4fe3-a9e3-408deaa4738b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x=[1,2,3]\n",
    "a=np.asarray(x)\n",
    "print(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "0a12511d-f771-47e7-9f9e-9a73307adf41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2]\n",
      " [3 4]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a = np.array([[1, 2], [3, 4]])\n",
    "print(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0d6b15bd-d04d-4be6-9fd8-1ae841e19226",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "list1 = [1, 2, 3, 4, 5]\n",
    "arr = np.array(list1)\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cd98a1fb-43a7-4741-b4ba-0b707a1b7f54",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[          0           0]\n",
      " [ -448711744         413]\n",
      " [          0 -2147483648]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x=np.empty([3,2],dtype=int)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6a852ffb-b06b-4d7e-9d38-891c9ca28786",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0.  5. 10. 15. 20.]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "vector = np.linspace(0, 20, 5)\n",
    "print(vector)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f826ddac-fbd0-44cf-8511-4eb3a7d6605a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[0. 0.]\n",
      "  [0. 0.]]\n",
      "\n",
      " [[0. 0.]\n",
      "  [0. 0.]]]\n",
      "[0. 0. 0. 0. 0. 0. 0. 0.]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr=np.zeros(8)\n",
    "arr3d=arr.reshape((2,2,2))\n",
    "print(arr3d)\n",
    "arr=arr3d.ravel()\n",
    "print(arr)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c9728b32-cf3f-45ba-a454-e2e7ec18bc4c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 3)\n",
      "2\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a=np.array([[1,2,3],[3,4,5],[4,5,6]])\n",
    "print(a.shape)\n",
    "print(a.ndim)\n",
    "print(a.itemsize)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "bd4d7ad9-6ffe-495b-8a9c-4534c8b34a69",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 3 5 7 9]\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr=np.arange(20)\n",
    "arr_slice=slice(1,10,2)\n",
    "element=arr[6]\n",
    "print(arr[arr_slice])\n",
    "print(arr[element])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e18eb7e2-c277-46d2-bd01-dcad9464ec6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0. 0. 0. 0. 0.]\n",
      " [0. 0. 0. 0. 0.]\n",
      " [0. 0. 0. 0. 0.]\n",
      " [0. 0. 0. 0. 0.]\n",
      " [0. 0. 0. 0. 0.]]\n"
     ]
    }
   ],
   "source": [
    "arr = np.zeros((5,5))\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "348d165d-9a69-49e6-a006-3cf854a1cfbe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0. 0. 0. 0. 0.]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x=np.zeros(5)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ad643b7-eb12-48dc-8dd4-a60c90aef188",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
