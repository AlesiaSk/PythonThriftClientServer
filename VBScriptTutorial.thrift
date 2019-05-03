struct ConstantsPart {
    1: required string title;
    2: required string text;
}
 
service TutorialService {
  void deleteChapter(1:string chapter)
  void addToChapter()
  list<string> getChapter()
}
