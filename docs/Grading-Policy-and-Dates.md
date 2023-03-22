# Grading Policy and Dates

[< back to specs](./)

## Table of Contents

- [Deadlines](#deadlines)
- [Core](#core)
- [Reach](#reach)
- [Showcase](#showcase)

## Deadlines

| Project Component   | Maximum Points | Due Date | How to Submit |
|:-------------------:|:--------------:|:--------:|:-------------:|
|Teams/Proposal       |      10        |   11/10  | Gradescope    |
|Warmup               |      10        |   11/26  | GitHub        |
|Core                 |      40        |   11/26  | GitHub        |
|Core Team Evaluation |      5         |   11/27  | Google Form   |
|Reach                |      50        |   12/11  | GitHub        |
|Final Team Evaluation|      5         |   12/14  | Google Form (Assignment 8) |
|Showcase             |      10        |   12/13  | Attendance + Presentation     |

## Core

The core will be completely autograded. However, unlike previous projects, ***you will not have access to the autograder before your final submission***. (This is out of fairness because other Final Projects cannot be autograded.) This means that you must test your code extensively before submitting.

The Warmup will be graded with the Core. We will only grade it against the public test cases contained in the Warmup's doctests.

We will treat your last code pushed to GitHub before the deadline as your final submission. You ***must*** use GitHub to submit your project. To verify your submission, navigate your web browser to your GitHub repository (CREATIVE_AI_<NUMBER>_REPOSITORY) and make sure that the files there are the files you want to submit. We will not grade late submissions, so make sure you are pushing your code to GitHub.

Please make sure that your code runs correctly before you submit it. We will deduct points from tests which result in syntax errors.

## Reach

The Reach will be graded by hand. We will download your project code from GitHub and run it as follows:

```python generate.py```

In order to understand your project, we require that you include a document called ```README.md``` in the root directory of your project. This will replace the ```README.md``` we have provided for you. This is where you will describe your project, any changes you have made from your proposal, and any other python libraries we need to run your code. The format of your ```README.md``` should follow this template:

```
- Team Name
- group member 1; uniqname 1
- group member 2; uniqname 2
- group member 3; uniqname 3
- group member 4; uniqname 4

All Downloaded Python Libraries used:
* Module 1
* Module 2
...

[Replace with Description of the Application (1-2 sentences)]
[Replace with Description of the Heuristics used (1-2 sentences)]
[Replace with Description of the Showmanship component (1-2 sentences)]

[Anything else you want to say.]
```

### Sample Proposal

```
- The Beatles
- John Lennon; jlennon
- Paul McCartney; mccartney
- George Harrison; hairygeorge
- Ringo Starr; ringstarrrrr

Python Libraries used:
* matplotlib
* pysynth

We used our learning model to generate songs in the musical style of polka. We refined our model by mixing in a backbeat generated using pysynth_b (the pysynth heuristics), and we reused sentences in order to make a more consistent song (the general heurisic). To showcase our project, we graphed the songs we produced in matplotlib.
```

We will treat your last code pushed to GitHub before the deadline as your final submission. You ***must*** use GitHub to submit your project. To verify your submission, navigate your web browser to your GitHub repository (**CREATIVE_AI_XXX_REPOSITORY**) and make sure that the files there are the files you want to submit. We will not grade late submissions, so make sure you are pushing your code to GitHub.

## Showcase

The Showcase is your chance to show off your project and celebrate your hard work.

In order to present your project, your group **must bring a laptop** so that you can demo your project in real time. Outlets will be scarce at the showcase, so make sure your laptop is charged. Additionally, if your project specialized in music generation, bring headphones -- the showcase will be loud.

At the Showcase staff members will come around to see your team demo your project. Every member of your group is expected to contribute equally to technical explanations of how the project was implemented and what you learned. This presentation will count for part of your grade. Every team will be graded by at least two different staff members.

Although we will primarily grade based on your technical explanation, we encourage you to get into the spirit of the Showcase. Have fun with it. Staff members, your fellow students, and even companies will come to look at your project. Here are a few ideas for how you can show your project off:

- Make it interactive. Let users run your learning models themselves.
- Make a playlist of your best songs to show off to listeners.
- If you create lyrics or poems, print them out and put them on a poster.
- If you've generated interesting graphs, print them out and put them on a poster.
- If you have a twitterbot, tweet with the hashtag "#eecs183".

Enjoy the Showcase and congratulations on finishing your semester of EECS 183!
