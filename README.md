# Optimizing-Information-Retrieval-with-IRSystem-Inverted-Index-and-K-gram-Index-using-Skiplists

The following functions can be run by:

1. **Stopword Removal :**

Import InfoRetSystem from Inverted\_index.py and create an object.

InfoRetSystem class has a function remove\_stopwords that takes the list of words for which the stop words should be removed.

Eg: let data = [“Information”,” Retrieval”, “ is”,”a”, “great”,”course”] To eliminate stopwords.

From Inverted\_index import InfoRetSystem IR = InfoRetSystem()

Filtered\_data = IR.remove\_stopwords(data))

Filtered\_data variable has the list of data that is stopword free **code:**

![Aspose Words 71a3c005-5641-4358-9a19-423db04fb889 001](https://github.com/Prod23/Optimizing-Information-Retrieval-with-IRSystem-Inverted-Index-and-K-gram-Index-using-Skiplists/assets/88609959/056c078c-1242-46b7-8960-7ca1eb139c6d)


**Result:**
![Aspose Words 71a3c005-5641-4358-9a19-423db04fb889 002](https://github.com/Prod23/Optimizing-Information-Retrieval-with-IRSystem-Inverted-Index-and-K-gram-Index-using-Skiplists/assets/88609959/d456566d-8c3c-4d1c-9a9e-b4db7e3bbd83)

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.002.png)

2. **Stemming/Lemmatization:**

Similarly in the InfoRetSystem, we have a function stemmer which takes list as an input and stems all the words.

**Eg: Code:**
![Aspose Words 71a3c005-5641-4358-9a19-423db04fb889 003](https://github.com/Prod23/Optimizing-Information-Retrieval-with-IRSystem-Inverted-Index-and-K-gram-Index-using-Skiplists/assets/88609959/c07cca20-8e03-4e52-8d55-2c4677ffa302)

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.003.png)

Result :
![Aspose Words 71a3c005-5641-4358-9a19-423db04fb889 004](https://github.com/Prod23/Optimizing-Information-Retrieval-with-IRSystem-Inverted-Index-and-K-gram-Index-using-Skiplists/assets/88609959/6a9b2c14-a66b-43e0-95ab-3df917d3a418)

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.004.png)

3. **Building Index:**

The class InfoRetSystem has a function buildIRSystem to build the invertedIndex. Put all the required files in the folder database and run the script.

**Eg:**

**Code:**
![Aspose Words 71a3c005-5641-4358-9a19-423db04fb889 005](https://github.com/Prod23/Optimizing-Information-Retrieval-with-IRSystem-Inverted-Index-and-K-gram-Index-using-Skiplists/assets/88609959/7e12fa9e-256f-427b-84cf-c6a9e3846548)

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.005.png)

**Output:**
![Aspose Words 71a3c005-5641-4358-9a19-423db04fb889 006](https://github.com/Prod23/Optimizing-Information-Retrieval-with-IRSystem-Inverted-Index-and-K-gram-Index-using-Skiplists/assets/88609959/b7bcb024-4629-49a5-bd2e-392b5872c58b)

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.006.png)

4. **Querying:**

The file ParseR has a function retrieveResults when given a query prints all the matching documents and other info about it.

Code:
![Aspose Words 71a3c005-5641-4358-9a19-423db04fb889 007](https://github.com/Prod23/Optimizing-Information-Retrieval-with-IRSystem-Inverted-Index-and-K-gram-Index-using-Skiplists/assets/88609959/c18a80d1-3383-48ff-9215-5dbdcf8ddc6a)

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.007.png)

Result:
![Aspose Words 71a3c005-5641-4358-9a19-423db04fb889 008](https://github.com/Prod23/Optimizing-Information-Retrieval-with-IRSystem-Inverted-Index-and-K-gram-Index-using-Skiplists/assets/88609959/3e8763c5-aa0b-48e5-a676-41ca029114f8)

![](Aspose.Words.71a3c005-5641-4358-9a19-423db04fb889.008.png)
