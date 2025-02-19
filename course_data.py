sample_data = {
    "roster": ["Student A", "Student B", "Student C"],
    "assignments": {
        "Assignment 1": {
            "weight": 40,
            "submissions": {"Student A": 95, "Student B": 80, "Student C": 87},
        },
        "Assignment 2": {
            "weight": 35,
            "submissions": {"Student A": 90, "Student B": 85},
        },
        "Assignment 3": {
            "weight": 25,
            "submissions": {"Student B": 93, "Student C": 82},
        },
    },
}

actual_data = {
    "roster": [
        "Student A",
        "Student B",
        "Student C",
        "Student D",
        "Student E",
        "Student F",
        "Student G",
        "Student H",
        "Student I",
        "Student J",
        "Student K",
        "Student L",
        "Student M",
        "Student N",
        "Student O",
        "Student P",
        "Student Q",
        "Student R",
        "Student S",
        "Student T",
        "Student U",
        "Student V",
        "Student W",
        "Student X",
        "Student Y",
        "Student Z",
    ],
    "assignments": {
        "Exam 3": {
            "weight": 10,
            "submissions": {
                "Student E": 86,
                "Student L": 66,
                "Student I": 76,
                "Student T": 97,
                "Student V": 90,
                "Student G": 75,
                "Student R": 80,
                "Student N": 100,
                "Student D": 80,
                "Student Z": 71,
                "Student J": 87,
                "Student F": 79,
                "Student C": 91,
                "Student A": 96,
                "Student K": 80,
                "Student M": 78,
                "Student W": 89,
                "Student X": 79,
                "Student Y": 100,
                "Student S": 81,
                "Student B": 82,
                "Student O": 83,
                "Student U": 85,
                "Student H": 95,
                "Student P": 71,
                "Student Q": 94,
            },
        },
        "Lab 8": {
            "weight": 2.5,
            "submissions": {
                "Student E": 94,
                "Student L": 75,
                "Student I": 80,
                "Student T": 100,
                "Student V": 89,
                "Student G": 74,
                "Student R": 79,
                "Student N": 100,
                "Student D": 79,
                "Student Z": 74,
                "Student J": 93,
                "Student F": 77,
                "Student C": 84,
                "Student A": 100,
                "Student K": 73,
                "Student X": 87,
                "Student Y": 100,
                "Student S": 82,
                "Student B": 85,
                "Student O": 84,
                "Student U": 83,
                "Student H": 97,
                "Student P": 66,
                "Student Q": 89,
            },
        },
        "Quiz 7": {
            "weight": 1.5,
            "submissions": {
                "Student E": 92,
                "Student L": 69,
                "Student I": 83,
                "Student T": 100,
                "Student V": 87,
                "Student G": 74,
                "Student R": 80,
                "Student N": 98,
                "Student D": 83,
                "Student Z": 73,
                "Student J": 84,
                "Student F": 76,
                "Student C": 89,
                "Student A": 97,
                "Student K": 73,
                "Student M": 78,
                "Student X": 83,
                "Student Y": 100,
                "Student S": 85,
                "Student B": 79,
                "Student O": 87,
                "Student U": 85,
                "Student H": 93,
                "Student P": 68,
                "Student Q": 92,
            },
        },
        "Quiz 6": {
            "weight": 1.5,
            "submissions": {
                "Student E": 91,
                "Student L": 74,
                "Student I": 83,
                "Student T": 93,
                "Student V": 96,
                "Student G": 75,
                "Student R": 77,
                "Student N": 100,
                "Student D": 76,
                "Student Z": 73,
                "Student J": 90,
                "Student F": 77,
                "Student C": 86,
                "Student A": 99,
                "Student K": 75,
                "Student M": 85,
                "Student W": 87,
                "Student X": 81,
                "Student Y": 99,
                "Student S": 81,
                "Student B": 85,
                "Student O": 81,
                "Student U": 82,
                "Student H": 89,
                "Student P": 66,
                "Student Q": 91,
            },
        },
        "Lab 1": {
            "weight": 2.5,
            "submissions": {
                "Student E": 86,
                "Student L": 67,
                "Student I": 75,
                "Student T": 96,
                "Student V": 96,
                "Student G": 74,
                "Student R": 80,
                "Student N": 95,
                "Student D": 75,
                "Student Z": 75,
                "Student J": 86,
                "Student F": 74,
                "Student C": 82,
                "Student A": 100,
                "Student K": 76,
                "Student M": 79,
                "Student X": 81,
                "Student Y": 100,
                "Student S": 84,
                "Student B": 83,
                "Student O": 80,
                "Student U": 82,
                "Student H": 94,
                "Student P": 65,
                "Student Q": 96,
            },
        },
        "Project 3": {
            "weight": 6,
            "submissions": {
                "Student E": 86,
                "Student L": 66,
                "Student I": 79,
                "Student T": 100,
                "Student V": 88,
                "Student G": 68,
                "Student N": 98,
                "Student D": 77,
                "Student Z": 77,
                "Student J": 87,
                "Student F": 74,
                "Student A": 100,
                "Student K": 78,
                "Student M": 84,
                "Student W": 86,
                "Student X": 86,
                "Student Y": 94,
                "Student S": 82,
                "Student B": 82,
                "Student O": 87,
                "Student U": 80,
                "Student H": 89,
                "Student P": 67,
                "Student Q": 93,
            },
        },
        "Quiz 8": {
            "weight": 1.5,
            "submissions": {
                "Student E": 94,
                "Student L": 70,
                "Student I": 84,
                "Student T": 100,
                "Student V": 88,
                "Student G": 76,
                "Student R": 78,
                "Student N": 100,
                "Student D": 76,
                "Student Z": 78,
                "Student J": 86,
                "Student F": 75,
                "Student C": 88,
                "Student A": 100,
                "Student K": 76,
                "Student M": 85,
                "Student W": 92,
                "Student Y": 96,
                "Student S": 80,
                "Student B": 84,
                "Student O": 87,
                "Student U": 84,
                "Student H": 96,
                "Student P": 66,
                "Student Q": 93,
            },
        },
        "Lab 2": {
            "weight": 2.5,
            "submissions": {
                "Student E": 88,
                "Student L": 66,
                "Student I": 79,
                "Student T": 98,
                "Student V": 91,
                "Student G": 68,
                "Student R": 72,
                "Student N": 100,
                "Student D": 83,
                "Student Z": 77,
                "Student J": 93,
                "Student F": 72,
                "Student C": 91,
                "Student A": 96,
                "Student K": 80,
                "Student M": 83,
                "Student W": 85,
                "Student X": 87,
                "Student Y": 100,
                "Student S": 78,
                "Student B": 81,
                "Student O": 83,
                "Student U": 80,
                "Student H": 91,
                "Student P": 73,
                "Student Q": 95,
            },
        },
        "Quiz 3": {
            "weight": 1.5,
            "submissions": {
                "Student E": 93,
                "Student L": 66,
                "Student I": 80,
                "Student T": 100,
                "Student V": 87,
                "Student R": 81,
                "Student N": 95,
                "Student D": 80,
                "Student Z": 74,
                "Student J": 92,
                "Student F": 74,
                "Student C": 89,
                "Student A": 100,
                "Student K": 73,
                "Student M": 82,
                "Student W": 89,
                "Student X": 86,
                "Student Y": 98,
                "Student S": 87,
                "Student B": 86,
                "Student U": 82,
                "Student H": 90,
                "Student P": 72,
                "Student Q": 90,
            },
        },
        "Exam 2": {
            "weight": 15,
            "submissions": {
                "Student E": 94,
                "Student L": 72,
                "Student I": 81,
                "Student T": 94,
                "Student V": 95,
                "Student G": 69,
                "Student R": 80,
                "Student N": 99,
                "Student D": 80,
                "Student Z": 69,
                "Student J": 87,
                "Student F": 78,
                "Student C": 91,
                "Student K": 80,
                "Student M": 87,
                "Student W": 89,
                "Student X": 84,
                "Student Y": 100,
                "Student S": 78,
                "Student B": 88,
                "Student O": 84,
                "Student U": 86,
                "Student H": 97,
                "Student P": 65,
            },
        },
        "Quiz 2": {
            "weight": 1.5,
            "submissions": {
                "Student E": 90,
                "Student L": 72,
                "Student I": 84,
                "Student T": 99,
                "Student V": 92,
                "Student G": 72,
                "Student R": 73,
                "Student N": 95,
                "Student D": 79,
                "Student Z": 69,
                "Student J": 93,
                "Student F": 74,
                "Student C": 84,
                "Student A": 100,
                "Student K": 78,
                "Student M": 85,
                "Student W": 89,
                "Student X": 86,
                "Student Y": 96,
                "Student S": 78,
                "Student B": 82,
                "Student O": 84,
                "Student U": 86,
                "Student H": 90,
                "Student P": 69,
                "Student Q": 95,
            },
        },
        "Lab 7": {
            "weight": 2.5,
            "submissions": {
                "Student E": 91,
                "Student L": 67,
                "Student I": 79,
                "Student T": 100,
                "Student V": 95,
                "Student G": 73,
                "Student R": 74,
                "Student N": 95,
                "Student D": 84,
                "Student Z": 73,
                "Student J": 90,
                "Student F": 72,
                "Student C": 91,
                "Student A": 96,
                "Student K": 76,
                "Student M": 79,
                "Student W": 89,
                "Student X": 86,
                "Student Y": 100,
                "Student S": 82,
                "Student B": 87,
                "Student O": 86,
                "Student U": 86,
                "Student H": 90,
                "Student P": 69,
                "Student Q": 89,
            },
        },
        "Exam 1": {
            "weight": 15,
            "submissions": {
                "Student L": 68,
                "Student I": 80,
                "Student T": 99,
                "Student V": 92,
                "Student G": 69,
                "Student R": 79,
                "Student N": 100,
                "Student D": 79,
                "Student Z": 77,
                "Student J": 93,
                "Student F": 75,
                "Student C": 91,
                "Student A": 95,
                "Student K": 78,
                "Student M": 82,
                "Student W": 86,
                "Student Y": 100,
                "Student S": 82,
                "Student B": 84,
                "Student O": 83,
                "Student U": 85,
                "Student H": 97,
                "Student P": 65,
                "Student Q": 90,
            },
        },
        "Quiz 1": {
            "weight": 1.5,
            "submissions": {
                "Student E": 88,
                "Student L": 71,
                "Student I": 79,
                "Student V": 92,
                "Student G": 75,
                "Student R": 79,
                "Student N": 96,
                "Student D": 78,
                "Student Z": 69,
                "Student J": 86,
                "Student F": 81,
                "Student C": 85,
                "Student A": 98,
                "Student K": 73,
                "Student M": 82,
                "Student W": 93,
                "Student X": 79,
                "Student Y": 100,
                "Student S": 85,
                "Student B": 88,
                "Student O": 81,
                "Student U": 79,
                "Student H": 96,
                "Student P": 68,
                "Student Q": 88,
            },
        },
        "Quiz 5": {
            "weight": 1.5,
            "submissions": {
                "Student E": 88,
                "Student L": 71,
                "Student I": 83,
                "Student T": 93,
                "Student V": 90,
                "Student G": 68,
                "Student R": 76,
                "Student N": 100,
                "Student D": 76,
                "Student Z": 72,
                "Student J": 85,
                "Student F": 75,
                "Student C": 86,
                "Student A": 100,
                "Student K": 77,
                "Student M": 84,
                "Student W": 88,
                "Student X": 84,
                "Student Y": 99,
                "Student S": 80,
                "Student B": 86,
                "Student O": 82,
                "Student U": 86,
                "Student H": 94,
                "Student P": 69,
                "Student Q": 94,
            },
        },
        "Project 4": {
            "weight": 10,
            "submissions": {
                "Student E": 91,
                "Student L": 67,
                "Student I": 81,
                "Student T": 93,
                "Student V": 92,
                "Student G": 74,
                "Student N": 100,
                "Student D": 75,
                "Student Z": 70,
                "Student J": 90,
                "Student F": 79,
                "Student C": 84,
                "Student A": 100,
                "Student K": 80,
                "Student M": 84,
                "Student W": 94,
                "Student X": 82,
                "Student Y": 97,
                "Student S": 87,
                "Student B": 80,
                "Student O": 79,
                "Student U": 85,
                "Student H": 95,
                "Student P": 69,
                "Student Q": 95,
            },
        },
        "Lab 6": {
            "weight": 2.5,
            "submissions": {
                "Student E": 86,
                "Student L": 73,
                "Student I": 78,
                "Student T": 98,
                "Student V": 94,
                "Student G": 74,
                "Student R": 75,
                "Student N": 97,
                "Student D": 82,
                "Student Z": 73,
                "Student J": 93,
                "Student F": 76,
                "Student C": 83,
                "Student A": 96,
                "Student K": 73,
                "Student M": 84,
                "Student X": 80,
                "Student Y": 100,
                "Student S": 79,
                "Student B": 83,
                "Student O": 84,
                "Student U": 81,
                "Student H": 90,
                "Student P": 72,
                "Student Q": 90,
            },
        },
        "Lab 3": {
            "weight": 2.5,
            "submissions": {
                "Student L": 67,
                "Student I": 82,
                "Student T": 100,
                "Student V": 91,
                "Student G": 70,
                "Student R": 72,
                "Student N": 94,
                "Student D": 83,
                "Student Z": 71,
                "Student J": 92,
                "Student F": 79,
                "Student C": 87,
                "Student A": 95,
                "Student K": 80,
                "Student M": 85,
                "Student W": 92,
                "Student Y": 99,
                "Student S": 83,
                "Student B": 81,
                "Student O": 78,
                "Student U": 81,
                "Student H": 93,
                "Student P": 71,
                "Student Q": 88,
            },
        },
        "Project 1": {
            "weight": 6,
            "submissions": {
                "Student L": 73,
                "Student I": 80,
                "Student T": 92,
                "Student V": 91,
                "Student G": 68,
                "Student R": 74,
                "Student N": 98,
                "Student D": 75,
                "Student Z": 76,
                "Student J": 89,
                "Student F": 78,
                "Student C": 86,
                "Student A": 100,
                "Student K": 76,
                "Student M": 85,
                "Student W": 87,
                "Student X": 86,
                "Student Y": 100,
                "Student S": 83,
                "Student B": 82,
                "Student O": 83,
                "Student U": 87,
                "Student H": 94,
                "Student P": 73,
                "Student Q": 89,
            },
        },
        "Quiz 4": {
            "weight": 1.5,
            "submissions": {
                "Student E": 94,
                "Student L": 72,
                "Student I": 80,
                "Student V": 96,
                "Student G": 75,
                "Student N": 97,
                "Student D": 75,
                "Student Z": 73,
                "Student J": 87,
                "Student F": 79,
                "Student C": 88,
                "Student A": 95,
                "Student K": 75,
                "Student M": 78,
                "Student W": 85,
                "Student X": 83,
                "Student Y": 96,
                "Student S": 87,
                "Student B": 83,
                "Student O": 86,
                "Student U": 78,
                "Student H": 95,
                "Student Q": 91,
            },
        },
        "Lab 4": {
            "weight": 2.5,
            "submissions": {
                "Student E": 87,
                "Student L": 71,
                "Student I": 82,
                "Student T": 97,
                "Student V": 90,
                "Student G": 76,
                "Student R": 81,
                "Student N": 96,
                "Student D": 78,
                "Student Z": 77,
                "Student J": 86,
                "Student F": 75,
                "Student C": 83,
                "Student A": 98,
                "Student K": 79,
                "Student M": 82,
                "Student W": 91,
                "Student X": 83,
                "Student S": 80,
                "Student B": 88,
                "Student O": 86,
                "Student U": 78,
                "Student H": 95,
                "Student P": 72,
                "Student Q": 92,
            },
        },
        "Project 2": {
            "weight": 6,
            "submissions": {
                "Student E": 88,
                "Student L": 75,
                "Student I": 79,
                "Student V": 94,
                "Student G": 69,
                "Student R": 78,
                "Student N": 97,
                "Student D": 81,
                "Student Z": 78,
                "Student J": 91,
                "Student C": 88,
                "Student A": 100,
                "Student K": 78,
                "Student M": 78,
                "Student X": 86,
                "Student Y": 95,
                "Student S": 86,
                "Student B": 88,
                "Student O": 79,
                "Student U": 84,
                "Student H": 96,
                "Student P": 67,
                "Student Q": 95,
            },
        },
        "Lab 5": {
            "weight": 2.5,
            "submissions": {
                "Student E": 89,
                "Student L": 72,
                "Student I": 78,
                "Student T": 92,
                "Student V": 87,
                "Student G": 75,
                "Student R": 80,
                "Student N": 100,
                "Student D": 82,
                "Student Z": 74,
                "Student J": 87,
                "Student F": 74,
                "Student C": 85,
                "Student A": 100,
                "Student K": 79,
                "Student M": 85,
                "Student W": 86,
                "Student X": 80,
                "Student Y": 100,
                "Student S": 83,
                "Student B": 88,
                "Student O": 83,
                "Student U": 85,
                "Student H": 95,
                "Student P": 73,
                "Student Q": 87,
            },
        },
    },
}