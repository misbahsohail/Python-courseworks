# Python-courseworks

`Cycle convert`

Write a function cycle_convert that takes a variable x as an input and a cycle step size n. It converts the type of x into another type and returns the converted x. The conversion is in the following a fixed order of Python types:
int → float → bool → string → complex
Further instructions:
• Cycle step size n controls how many steps you go. For instance, for n=1, an int is converted to float, a string is converted to complex, and so on. For n=2, an int is
converted to bool (skipping the conversion to float), or a float is converted to string (skipping the conversion to bool).
• Sometimes conversion is not possible. For instance, you cannot convert random words to numbers, but you needn’t worry about this. Assume all the conversions are
possible.
• Wrap around: When the step size brings you beyond the end of the conversion order, you start from the beginning. For instance, for n=2, a complex type is converted to
float. Or for n=4, a string is converted to bool.
• Negative step size: if n negative, the cycle goes to the left. For instance, for n=-1, a complex type is converted to string, or a bool type is converted to float.
• The default value for n is 1.

Examples:
• If x=2 is an integer, then cycle_convert(x, 1) returns a float, and cycle_convert(x, 2) returns a Boolean
• If x=”10” is a string, then cycle_convert(x, 1) returns the complex number 10+0j, cycle_convert(x, 2) returns the interger 10, and cycle_convert(x, 3) returns the float 10.0.


`Unit translator`

Write a function unit_translator(filename, D) that converts all length, filesize, and time units written in a text file to target units. The text file with converted units is then written out to a new text file; the filename of the new file is the name of the original file appended with ‘_translated’ (e.g. “example_text.txt” becomes “example_text_translated.txt”).
Filename is a string that specifies the name of the input text file.
D is a dictionary that specifies to which units lengths, filesizes, and times are to be converted.

Further instructions:
• The following types of units must be covered
  o length units: km, m, cm, mm
  o filesize units: B (for bytes), KB, MB, GB, TB, PB
  o time units: sec (for seconds), min, h
• They are specified in dictionary D, e.g. D = {‘length’ : ‘km’, ‘filesize’ : ‘GB’ , ‘time’ : ‘h’}.
• If the dictionary does not contain a particular key, the respective unit is notconverted.
  o Example: if D = {‘length’ : ‘km’}, then only lengths get converted. Filesizes and times would not get converted.
• Filename can be an absolute or relative path.
• It is up to you whether integers are given in float or integer notation (e.g. converting “1024 MB” to either “1 GB” or “1.0 GB” are both correct solutions).

To give an example, consider the example text provided in the file Q2_example_text.txt:
At 2 h after starting the programme, the GPU was consuming about 12 GB at the time. Each chip had a length of 5.3 cm and the width was about 10 mm. Over time, VRAM memory consumption rose beyond the 16 GB limit and the programme crashed, though it ran really just short of 1024 MB. With better coding, some GB might have been saved. It just took 120 sec to restart the programme.

Applying the unit translator with the function call unit_translator(filename, {'length' : 'cm', 'filesize':'GB'})
we obtain the following translated text (saved by the function in the file Q2_example_text_translated.txt):

At 2 h after starting the programme, the GPU was consuming about 12.0 GB at the time. Each chip had a length of 5.3 cm and the width was about 1.0 cm. Over time,
VRAM memory consumption rose beyond the 16.0 GB limit and the programme crashed, though it ran really just short of 1.0 GB. With better coding, some GB might
have been saved. It just took 120 sec to restart the programme.


`Lambda machine`

A lambda expression represents an anonymous Python function. It can be used as a shorthand notation for simple Python functions. Write a function called lambda_machine
that takes a filename for a Python file (e.g. “mytest.py”) as an input. The function parses the contents of the file and outputs a new file with “lambda_” prepended (e.g.“lambda_mytest.py”).

• If the code contains a def statement, it is being translated into a lambda function.
• Code that already represents a lambda function remains unchanged. Code that just contains a nested lambda function is removed, see these following example lines of
code:
  o add = lambda x,y : return x+y à remains unchanged
  o d = sorted(d.items(), key = lambda x:x[1], reverse=True) à gets removed
• Any code that is not part of a function or a lambda function should be ignored/removed from the output.
• If there is multiple def statements, the same number of lambda functions needs to be produced.
• Your solution needs to be able to deal with if-elif-else statements in the function body.
• Your solution does not need to handle other situations such as functions defined within functions, or for/while loops.

Simple example:
Consider the file mytest.py which contains the following function:

def add(a,b,c):
  return a + b + c

Then lambda_machine should output a file that contains the function in lambda notation as follows:

add = lambda a,b,c: a + b + c


`Processing Wikipedia pages`

In this exercise you will work with the wikipedia package (version 1.4) for Python. It provides an interface to the content of Wikipedia pages. You can install version 1.4 by e.g. typing pip install wikipedia==1.4 on the command line.

Q1.1) Write a function wikipage2file(wikipedia_pagetitle, output_filepath), which takes as input two arguments: a string for the title of a Wikipedia page and a string
representing an output folder where the output will be saved. The function performs the following operations.
(1) Searches all Wikipedia pages that can be retrieved with the wikipedia_pagetitle string.
(2) Retrieves the first candidate Wikipedia page and obtains two strings: the title and the content of that page.
(3) Writes a text file named wikipage.txt, where wikipage should be replaced by the Wikipedia page's title (but remove spaces in the filename). The resulting page should have, in the first line, the title, then two blank lines, and then the content of the page.

Q2.2) Write a function similar(x,y) that returns a float number based on the following:
Given two Wikipedia pages x and y, it calculates how similar they are based on the following operations:
(1) Compute the set containing every word that occurs in x at least once. Do the same for y.
(2) Obtain the set of the words that are contained both in x and in y.
(3) Obtain the set of all the words contained in x or y (including words contained in both x and y).
(4) Return the result of dividing the length of the set in (2) by the length of the set in (3).

The function should always return a value between 0 and 1 (with 0 being no similarity).


`Pandas & Visualisation`

You are given the csv file orders_cardiff_drinks.csv with a few thousand sales made by a company called Cardiff Drinks. This company sells wine, soda and juice. The csv file has information about the order id, the client id, when the order was made, the quantity (qty) of each of the three products the company sells (soda, wine and juice), the money spent in each product (in gbp), and the totals for quantity and money. Read this file using Pandas' read_csv() method and answer the following questions:

Q2.1 (visualization). Produce a bar plot that shows, for each year, the quantity sold for each product.
Q2.2 (visualization). Produce a correlation matrix and heatmap visualization between gbp and qty values for soda, juice and wine.
Q2.3 (answering questions). To answer the following questions, write Python code for querying the dataframe you have loaded with read_csv():
  • How many orders were placed in 2016?
  • Which client has purchased the greatest number of soda bottles overall?
  • In which weekday is wine sold the most on average (across the whole sales history)?
  • Which drink was the most popular (in GBP) in winter (from Dec 21st to March 21st)?
  Break your answer down for each year.
  • In which year-month (e.g. January 2015) was there the highest number of orders in which the quantity of wine bottles was higher than the average for that year?
  
NumPy uses broadcasting to perform mathematical operations on pairs of arrays that do not have the same size in each dimension or not the same number of dimensions. The limitation of broadcasting is: If none of the arrays has size 1 in the mismatched dimension, NumPy’s broadcasting fails. Therefore, we here want to extend the broadcasting capabilities of NumPy:

Imagine the shapes of two arrays are mismatched in a given dimension. If one of the sizes is a multiple of the other (e.g. 6 is a multiple of 3), the smaller array gets repeated within that dimension (e.g., so both arrays have size 6). Then, the mathematical operation is applied.

Example: Let us define the array a with shape (4, 3) as

1, 2, 3
4, 5, 6
7, 8, 9,
10,11,12

and the array b with shape (2,3) as

10, 20, 30
40, 50, 60

then their sum broadcast(np.add, a, b) is given by

11, 22, 33
44, 55, 66
17, 28, 39,
50, 61, 72

which has shape (4,3).

Detailed instructions:
• Write a function broadcast(fun, a, b) that takes the arguments fun, a and b.
Here a and b are the NumPy arrays and fun represents the arithmetic function (e.g. np.add). It returns an ndarray which is the result of the operation fun applied to the two arrays using appropriate broadcasting (right side in the example figure). The solution needs to work with all basic mathematical operations, that is addition,
subtraction, multiplication, division, and taking a power needs to be implemented.
• a and b can have a different number of dimensions.
• a and b can have mismatches on one, multiple, or even all dimensions, e.g. (6, 2, 3) and (3, 4, 1).
• Extended broadcasting is possible if for any dimension the size of one array is a multiple of the size of the other array. This is the case for e.g. arrays with shape (6, 2, 3) and (3, 4, 1).
• If broadcasting is not possible even under the extended rule, you should print 'Cannot broadcast' and return None.


`What is the long form of the acronym?`

In this question, your task is to implement several functions that parse text strings for acronyms and their long forms. Acronyms are abbreviations typically formed from the initial letters of multiple words and pronounced as a word. For instance, the acronym "GPU" stands for the long form "graphics processing unit". In this question, an acronym is defined as a character sequence of at least two successive capital letters. Your task is to implement several functions that together parse a text for acronyms and find their long forms.

As an example text, let us define the string
s = "A GPU, which stands for graphics processing unit, is different from CPUs, says the IT expert. For some operations, a GPU is faster than a CPU. GPUs are not always faster though."

Q1 a) Parse acronyms
Write a function read_file(filename) that receives as input a filename. The filename includes the filepath. The function returns the entire content of the file as a single string.
Write a function find_acronyms(s) that receives as input a string s representing the text. The function returns a list of acronyms. For our example above, find_acronyms(s) returns the list ['GPU', 'CPU', 'IT']. Note: It is not important in which order the acronyms appear in the returned list.

Q1 b) Find the long forms
In this question the hard work is done: given the acronyms, your task is to find their long form in the text. To this end, write a function find_long_forms(s, acronyms). It receives as input a string s representing the text and a Python list of acronyms. The function returns a dictionary d with key-value pairs, where the key is the acronym and the value is its long form. For instance, in our example above the output is the dictionary d = {'GPU' : 'graphics processing unit', 'CPU' : None, 'IT' : None}.

You can make the following assumptions:
• The long form is found in the same sentence as the acronym itself.
• If the acronym occurs multiple times in a text, its long form is found in the first sentence that contains the acronym.
• Every '.' (dot) marks the end of a sentence. Sentences like "I talked to the Dr. and raised my concerns." where dots are contained within the sentence will not occur.
• The first letter of the acronym is the same letter as the first letter of the first word of the long form. All of the letters in the acronym need to appear in the long form.
• If no long form can be found for an acronym, it is set to None (Python's None type) as in the dictionary above.

Q1 c) Replace acronyms by long forms
Assume we want to make the document more self-explanatory and replace its acronyms with their corresponding long forms. To this end, write a function replace_acronyms(s, d). It receives as input a string s representing the text, and a dictionary d which contains <acronym: long_form> key-value pairs as defined in Q1b). The function returns another string as output. In this output, all acronyms in s have been replaced with their long forms. The following rules apply:

- If an acronym has a long form, the sentence wherein the long form was defined remains unchanged. For any other sentence, the acronym is replaced by the long form.
- If an acronym has no long form, it is not replaced anywhere.
- If you add the long form at the beginning of a sentence, make sure that its first word is capitalised.

For instance, in our example above the output of the function is the string:
"A GPU, which stands for graphics processing unit, is different from CPUs, says the IT expert. For some operations, a graphics processing unit is faster than a CPU. Graphics processing units are not always faster though."
