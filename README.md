# gpt_dev

pip install -r requirements.txt

V1 Overall flow:
1. User inputs link to repo and prompt/documentation/ticket/coding standards etc.
2. Model asks any clarifying questions
3. Model creates PR
    (maybe another call to assess / edit the PR? Does the quality go up with a bunch of calls?)
4. Optional loop of
    a. additional feedback
    b. updated PR

More granular view

- (Done) Represent entire repo as block of text. Possibly this can be done better with sequential calls to the model summarizing relevant parts of each file or something
    - Github api to iterate through all files and get contents?
    - How does the repo chat thing that exists do this?

- How do I know whether there should be a message from the user with clarifications, or straight to pr gen?

- How to create PR? How to specify content of different files? Need to give the model the github api docs?
    