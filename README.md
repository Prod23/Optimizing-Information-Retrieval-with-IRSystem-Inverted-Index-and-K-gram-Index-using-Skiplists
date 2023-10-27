# Optimizing-Information-Retrieval-with-IRSystem-Inverted-Index-and-K-gram-Index-using-Skiplists

The following functions can be run by:

1. **Stopword Removal :**

Import InfoRetSystem from Inverted\_index.py and create an object.

InfoRetSystem class has a function remove\_stopwords that takes the list of words for which the stop words should be removed.

Eg: let data = [“Information”,” Retrieval”, “ is”,”a”, “great”,”course”] To eliminate stopwords.

From Inverted\_index import InfoRetSystem IR = InfoRetSystem()

Filtered\_data = IR.remove\_stopwords(data))

Filtered\_data variable has the list of data that is stopword free **code:**

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.001.png)

**Result:**

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.002.png)

2. **Stemming/Lemmatization:**

Similarly in the InfoRetSystem, we have a function stemmer which takes list as an input and stems all the words.

**Eg: Code:**

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.003.png)

Result :

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.004.png)

3. **Building Index:**

The class InfoRetSystem has a function buildIRSystem to build the invertedIndex. Put all the required files in the folder database and run the script.

**Eg:**

**Code:**

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.005.png)

**Output:**

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.006.png)

4. **Querying:**

The file ParseR has a function retrieveResults when given a query prints all the matching documents and other info about it.

Code:

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.007.png)

Result:

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.008.png)
