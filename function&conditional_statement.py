{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNSxSYSPZA8kJzxBK5Vj+yP",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/festuge/function-conditional.statement/blob/main/function%26conditional_statement.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "How to test functions using Python Doctests\n"
      ],
      "metadata": {
        "id": "tYmPzrT6WrPS"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "9LOXGCPDWpK6"
      },
      "outputs": [],
      "source": [
        "#automated testing\n",
        "import doctest"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def add_numbers(a, b):\n",
        "  \"\"\"This function takes twominputs, sum them and return the result\n",
        "  >>> add_numbers(2, 3)\n",
        "  5\n",
        "  >>> add_numbers(10, 2)\n",
        "  12\n",
        "  >>> add_numbers(4, 3)\n",
        "  7\n",
        "  \"\"\"\n",
        "  return a+b"
      ],
      "metadata": {
        "id": "FuwxbuT8XAYD"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "add_numbers(7,8)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IQFZ52XxX2IG",
        "outputId": "28d711d6-63df-4b48-ccaf-af7eee43266c"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "15"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "What are built-in functions?\n",
        "pyhthon comes with some helpful \"built-in\" functions that are simply part of the python language and help us do operations"
      ],
      "metadata": {
        "id": "6lKnjtBbYnGI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# ptint\n",
        "print(\"forcefully print out whatever you pass\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "70SqYoJjY_pf",
        "outputId": "95ab167f-d4c2-40e6-d795-1e9304425f65"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "forcefully print out whatever you pass\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#let's see the data type of bmi_joe:\n",
        "joe_bmi = 27.5\n",
        "type(joe_bmi)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pxEJKKIqajtK",
        "outputId": "12922a28-2ab4-431c-bfc9-a39b4683f92c"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "float"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "some built in function works well with list."
      ],
      "metadata": {
        "id": "MJvvbUPfZdGZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# lets save a collection of data in a list\n",
        "this_is_a_string = (\"claud\", 50, 80, 170, \"parrot\")\n",
        "values = (11.82, 65, 48, 58, 55)\n",
        "print(values)\n",
        "print(this_is_a_string)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jQtJXmhSZZSX",
        "outputId": "c78a61a1-d623-42be-925f-f929a3b5da0a"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(11.82, 65, 48, 58, 55)\n",
            "('claud', 50, 80, 170, 'parrot')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "we can output the value of a list using \"len\""
      ],
      "metadata": {
        "id": "BvyQ1wE3aIAk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "len(\"value\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cgjyzl-xaMGv",
        "outputId": "6ba2fa39-cee8-413d-ee5a-f7e13c0ba4cb"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "values"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pbyVi3lDcLks",
        "outputId": "8c9eb8b8-33e6-49c4-e10c-c6cc74ee00a5"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(11.82, 65, 48, 58, 55)"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#smallest value:\n",
        "min(values)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P828AfUjcNu0",
        "outputId": "967f741d-7054-4da7-a0a5-49442c530177"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "11.82"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#largest value:\n",
        "max(values)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uCvoOcjdcgRU",
        "outputId": "1506bfa3-be21-4c93-9672-06f443251d4e"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "65"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#sort the values:\n",
        "sorted(values)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pHj35qZbck_3",
        "outputId": "c25a1498-1744-4166-b891-8f7ad418c245"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[11.82, 48, 55, 58, 65]"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "docs.python.org"
      ],
      "metadata": {
        "id": "RW4A17Coc2vJ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "a special built-in function: help()\n",
        "it pulls up documents of other functions"
      ],
      "metadata": {
        "id": "1dStJwakc6Tr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "help(sorted)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V7VgILr1cqvM",
        "outputId": "25810e69-e61b-4b77-df58-5ca75ef772a9"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Help on built-in function sorted in module builtins:\n",
            "\n",
            "sorted(iterable, /, *, key=None, reverse=False)\n",
            "    Return a new list containing all items from the iterable in ascending order.\n",
            "    \n",
            "    A custom key function can be supplied to customize the sort order, and the\n",
            "    reverse flag can be set to request the result in descending order.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "values"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-doLr1Pwdc4a",
        "outputId": "65513be1-2b70-40d4-db45-f64fa6c423f2"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(11.82, 65, 48, 58, 55)"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sorted(values)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "O9JAIDrvdd3K",
        "outputId": "0675cbb1-4c13-4a7f-e789-f6ef0a5038e5"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[11.82, 48, 55, 58, 65]"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "?sorted"
      ],
      "metadata": {
        "id": "5cAL1Jh1dmva"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "?sorted"
      ],
      "metadata": {
        "id": "1Fn0XvJ5dg3L"
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Methods: build-in function for different data types"
      ],
      "metadata": {
        "id": "Qsm20BeDdzyi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#remember how different data types "
      ],
      "metadata": {
        "id": "qUqUtpafd8bP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "String Methods"
      ],
      "metadata": {
        "id": "OUofQI87etOC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#string\n",
        "my_string = \"this is a string\""
      ],
      "metadata": {
        "id": "_411Yso6exIb"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "my_string.upper()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "JFvydfgVe7Dq",
        "outputId": "c0103cd0-879b-48a1-ec58-baaeca2d60ec"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'THIS IS A STRING'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "capitalize"
      ],
      "metadata": {
        "id": "PFe-5o31fUdf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#capitalize\n",
        "my_string.capitalize()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "Yc_w_FrSfWS8",
        "outputId": "99321c8f-a7cf-418e-f9aa-5e502f429b13"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'This is a string'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "len(my_string.split())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4v-0ylOxidw-",
        "outputId": "8e4e170f-67ac-410f-e71f-7a197cddc1e7"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "check \n",
        "www.programiz.com"
      ],
      "metadata": {
        "id": "YzDIjJaMfllH"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "split"
      ],
      "metadata": {
        "id": "_wIcJADIf3-_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#split\n",
        "my_string"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "YEnINoTlfsbD",
        "outputId": "abf71fe2-4a60-4c15-ae46-a95b16984e2b"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'this is a string'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "my_string.split()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "74B63olTf8wp",
        "outputId": "5f8eee4a-9d27-4a78-cd9e-2e880dad11c6"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['this', 'is', 'a', 'string']"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "List methods. we have already used a few list methods when working with list. we have used methods like .append(), .pop(), .remove(), and .insert()"
      ],
      "metadata": {
        "id": "KOX73xc7hDKH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "weekdays = [\"Monday\", \"Tuesday\", \"Wednesday\", \"Thursday\"]"
      ],
      "metadata": {
        "id": "Va_f7-J5gCnO"
      },
      "execution_count": 100,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#finnd the index position of an element in the list:\n",
        "weekdays.index(\"Wednesday\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UFV2A-LShvJh",
        "outputId": "dc2b900f-cec0-4aa5-a244-298236f52eb8"
      },
      "execution_count": 101,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {},
          "execution_count": 101
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#don't work accross the board\n",
        "weekdays.remove(\"Tuesday\")\n",
        "weekdays"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NnYWsGhTi6PQ",
        "outputId": "39973da8-1a72-40b9-b872-a52b06c589c6"
      },
      "execution_count": 102,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Monday', 'Wednesday', 'Thursday']"
            ]
          },
          "metadata": {},
          "execution_count": 102
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "weekdays.append(\"Friday\")\n",
        "weekdays"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N6EcnCtTuqqP",
        "outputId": "eed809cf-6bb9-4cf7-eac3-1d533a3cf7a8"
      },
      "execution_count": 121,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Monday', 'Wednesday', 'Thursday', 'Friday']"
            ]
          },
          "metadata": {},
          "execution_count": 121
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Looping functions"
      ],
      "metadata": {
        "id": "WF48MfoPjvJc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#a list of lists (or a nested list) of people's names, heights, weights in meters:\n",
        "students = [\n",
        "    [\"Joe\", 1.82, 84.2],\n",
        "    [\"Susan\", 1.59, 56.3],\n",
        "    [\"Holly\", 1.66, 59.1],\n",
        "    [\"Meghan\", 1.61, 50.8],\n",
        "    [\"Mike\", 1.79, 81.3],\n",
        "    [\"Roger\", 1.85, 85.5],\n",
        "    [\"Jane\", 1.65, 54.9],\n",
        "    [\"Maria\", 1.61, 52.6],\n",
        "    [\"Douglas\", 1.91, 89.2],\n",
        "    [\"Sam\", 1.86, 86],\n",
        "]"
      ],
      "metadata": {
        "id": "wfRV10Uojv01"
      },
      "execution_count": 103,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "students"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xmSj4hE1kf2l",
        "outputId": "4f434463-6746-4809-ea18-ea8defeb6c74"
      },
      "execution_count": 104,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[['Joe', 1.82, 84.2],\n",
              " ['Susan', 1.59, 56.3],\n",
              " ['Holly', 1.66, 59.1],\n",
              " ['Meghan', 1.61, 50.8],\n",
              " ['Mike', 1.79, 81.3],\n",
              " ['Roger', 1.85, 85.5],\n",
              " ['Jane', 1.65, 54.9],\n",
              " ['Maria', 1.61, 52.6],\n",
              " ['Douglas', 1.91, 89.2],\n",
              " ['Sam', 1.86, 86]]"
            ]
          },
          "metadata": {},
          "execution_count": 104
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "students[0]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Dxx47dvXkhG-",
        "outputId": "d80f6e3f-bf61-462a-ee75-ca8c017e7b87"
      },
      "execution_count": 105,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Joe', 1.82, 84.2]"
            ]
          },
          "metadata": {},
          "execution_count": 105
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "students[2]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yQBaiM1ckmYw",
        "outputId": "f0ee72e9-bd53-4dff-ad6b-f03cf8d65678"
      },
      "execution_count": 106,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Holly', 1.66, 59.1]"
            ]
          },
          "metadata": {},
          "execution_count": 106
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = students[0]"
      ],
      "metadata": {
        "id": "i_GUR238kpkf"
      },
      "execution_count": 107,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E-0GtCdskyAy",
        "outputId": "cfd2bfab-2088-45e3-db62-b5dbb26189a4"
      },
      "execution_count": 108,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Joe', 1.82, 84.2]"
            ]
          },
          "metadata": {},
          "execution_count": 108
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x[0]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "NjTKpsURky-3",
        "outputId": "57c58bc2-c5ba-414f-92cf-8dce52b432bb"
      },
      "execution_count": 109,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Joe'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 109
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x[1]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m8NC3X-5k3yr",
        "outputId": "bd847819-0bc2-4af3-d214-bbefbdc2694a"
      },
      "execution_count": 110,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1.82"
            ]
          },
          "metadata": {},
          "execution_count": 110
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x[2]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m0NTaKq0k8TV",
        "outputId": "5a4811f1-fb70-4e83-8c4b-1092fc99968e"
      },
      "execution_count": 111,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "84.2"
            ]
          },
          "metadata": {},
          "execution_count": 111
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "Joe_bmi = x[2]/(x[1]**2)\n",
        "Joe_bmi"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kHK7uODPk-4W",
        "outputId": "369a32c8-b7cf-4ca2-df9c-1d56dfa96238"
      },
      "execution_count": 112,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "25.4196353097452"
            ]
          },
          "metadata": {},
          "execution_count": 112
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "cMuFi1jHlJsw"
      },
      "execution_count": 112,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "susan_bmi = students[1][2]/(students[1][1]**2)\n",
        "susan_bmi"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AjhfikpUlcXo",
        "outputId": "c3c01c19-742a-4879-d1a9-5cfd7fe6eb70"
      },
      "execution_count": 113,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "22.26968869902298"
            ]
          },
          "metadata": {},
          "execution_count": 113
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y = students[1]\n",
        "susan_bmi = y[2]/(y[1]**2)\n",
        "susan_bmi"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3-_0_NDvlyvx",
        "outputId": "55babb05-86da-4951-b06a-90b0fb60c189"
      },
      "execution_count": 114,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "22.26968869902298"
            ]
          },
          "metadata": {},
          "execution_count": 114
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def multiple_bmi(list):\n",
        "  '''\n",
        "  function to calculate individual BMIs\n",
        "  Parameters: a nested list of names, height, and weights\n",
        "  Returns: a list of names and their BMI\n",
        "  '''\n",
        "  bmis = []\n",
        "  #empty list that we'll add things to later\n",
        "  for x in list:\n",
        "    #for loop specifying each row in our list of people\n",
        "    y = x[2]/x[1]**2\n",
        "    z = [ x[0], y ]\n",
        "    print(z)\n",
        "    bmis.append(z)\n",
        "    #adds the name and BMI result to our empty list using indexing\n",
        "    #done in 2 steps because append() only takes 1 arguement at a time\n",
        "  return bmis\n",
        "  #returns our list, now filled with names and BMI"
      ],
      "metadata": {
        "id": "ZX5sPFxGmeX0"
      },
      "execution_count": 119,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "multiple_bmi(students)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WLZkhRDurzIs",
        "outputId": "b97d00f5-37a6-40e0-f041-04e730c180a7"
      },
      "execution_count": 120,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Joe', 25.4196353097452]\n",
            "['Susan', 22.26968869902298]\n",
            "['Holly', 21.447234722020614]\n",
            "['Meghan', 19.59800933605956]\n",
            "['Mike', 25.373739895758558]\n",
            "['Roger', 24.981738495252007]\n",
            "['Jane', 20.16528925619835]\n",
            "['Maria', 20.292426989699468]\n",
            "['Douglas', 24.45108412598339]\n",
            "['Sam', 24.858365128916635]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[['Joe', 25.4196353097452],\n",
              " ['Susan', 22.26968869902298],\n",
              " ['Holly', 21.447234722020614],\n",
              " ['Meghan', 19.59800933605956],\n",
              " ['Mike', 25.373739895758558],\n",
              " ['Roger', 24.981738495252007],\n",
              " ['Jane', 20.16528925619835],\n",
              " ['Maria', 20.292426989699468],\n",
              " ['Douglas', 24.45108412598339],\n",
              " ['Sam', 24.858365128916635]]"
            ]
          },
          "metadata": {},
          "execution_count": 120
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Python packages: \n",
        "What is a package?: python's super powers. other people have written a bunch of code to handle just about any task."
      ],
      "metadata": {
        "id": "c3w2Qw90xvSY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Packages: need to do x? there's a package for that!\n",
        "#Meet your first package:math -- comes with mathematical functions like sine, cosine, arctan, square rrot, etc\n",
        "import math\n",
        "math.sqrt(4)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W6DherE8v92N",
        "outputId": "8c9dfc7e-a364-4930-bdd2-3caa9c8baf9a"
      },
      "execution_count": 123,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2.0"
            ]
          },
          "metadata": {},
          "execution_count": 123
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import math as m\n",
        "m.sqrt(16)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hbHpytVkyVOY",
        "outputId": "958296f0-9c9e-44f5-b6fc-34c4dc9e42dc"
      },
      "execution_count": 124,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4.0"
            ]
          },
          "metadata": {},
          "execution_count": 124
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "What if we only wanted module from Math? python allows you to select specific"
      ],
      "metadata": {
        "id": "-IqUmoqyzZ_n"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from math import sqrt\n",
        "sqrt(9)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "19VLpRtEy1sL",
        "outputId": "39f91062-93aa-422f-9dd6-6f76b4da2ab2"
      },
      "execution_count": 125,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3.0"
            ]
          },
          "metadata": {},
          "execution_count": 125
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "python 'IF' statments. run code only if certain conditions are met"
      ],
      "metadata": {
        "id": "H4crGMR10Dui"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "if 4 > 5:\n",
        "  print(\"Four is greater than five\")"
      ],
      "metadata": {
        "id": "sfZWxKpLzze3"
      },
      "execution_count": 126,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "if 5 > 4:\n",
        "  print(\"Five is greater than four.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JpDLk7IQ0aN2",
        "outputId": "9664eef3-39af-4f63-f08c-277869057d6d"
      },
      "execution_count": 127,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Five is greater than four.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Comparison operators:\n",
        "== equality\n",
        "!= inequality(not equal to)\n",
        "> greater than\n",
        "< the less than\n",
        ">= greater than or equal to\n",
        "<= less than or equal to"
      ],
      "metadata": {
        "id": "Io1BmqZ_0tUP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "5 == 4"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6eBy1RcY0jaQ",
        "outputId": "ff12e199-8e97-4bdc-d001-0998446f4d33"
      },
      "execution_count": 128,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 128
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "4 != 5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wqDoiGNJ1O-n",
        "outputId": "b3508852-0aeb-4196-96f2-6790a1a3f3c2"
      },
      "execution_count": 130,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 130
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "The ELSE condition"
      ],
      "metadata": {
        "id": "SqEfnOaC1Tos"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "money_in_wallet = 5.00\n",
        "movie_ticket_price = 8.99\n",
        "\n",
        "if money_in_wallet >= movie_ticket_price:\n",
        "  print(\"Go to the movies!\")\n",
        "else:\n",
        "  print(\"Stay home and watch netflix\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r6QIOPpQ1SC1",
        "outputId": "2b9d8f9d-7a36-4465-e326-91e0f4d03b43"
      },
      "execution_count": 131,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Stay home and watch netflix\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "the ELIFE condition"
      ],
      "metadata": {
        "id": "PirzJs9i16NN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "visitor = \"George\"\n",
        "if visitor == \"Bryce\":\n",
        "  print(\"Hi Bryce!\")\n",
        "elif visitor == \"Jacob\":\n",
        "  print(\"Hi Jacob!\")\n",
        "elif visitor == \"Ben\":\n",
        "  print(\"Hi Ben!\")\n",
        "else:\n",
        "  print(\"Please to meet you!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2dhLe3j419ud",
        "outputId": "461139de-eacd-41ca-9848-8b5be11e6250"
      },
      "execution_count": 132,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please to meet you!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "The 'in' keyword"
      ],
      "metadata": {
        "id": "ds5Ynjbe2rVT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "friends = [\"Bryce\", \"Jacob\", \"Mike\", \"Ben\", \"Young\"]\n",
        "visitor = \"Mike\"\n",
        "if visitor in friends:\n",
        "  print(\"Hi\" + visitor + \"!\")\n",
        "else:\n",
        "  print(\"Please to meet you!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0HWc8BwT2vHZ",
        "outputId": "32c40da3-561d-4089-b645-51cf3601f69f"
      },
      "execution_count": 133,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "HiMike!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Logical operators\n",
        "'and'\n",
        "'or'"
      ],
      "metadata": {
        "id": "FPq_VpBA3ZvL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "wants_to_learn_data_science = True\n",
        "will_work_hard = True\n",
        "age = 20\n",
        "\n",
        "if age >= 18 and wants_to_learn_data_science and will_work_hard:\n",
        "  print(\"Go to OSTEMB School!\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wgsn7LpN3i2c",
        "outputId": "1f5350e5-71bf-4f22-cb08-4f7818066fb1"
      },
      "execution_count": 134,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Go to OSTEMB School!\n"
          ]
        }
      ]
    }
  ]
}