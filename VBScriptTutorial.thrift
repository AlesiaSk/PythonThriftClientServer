struct ConstantsPart {
    1: required string title;
    2: required string text;
}
 
service TutorialService {
  void getConstants()
  list<string> getChapter()
}
