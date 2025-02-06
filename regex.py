import re;
st = "// This is a sample input file\n\
x = 10  // Assign value\n\
y = 20  // Another assignment\n\
\n\
/*\n\
This is a multi-line comment.\n\
It spans several lines.\n\
*/\n\
\n\
z = x + y  // Add values\n\
print(z)  // Output result\n\
";
st = re.sub(r"//.+", "",st);
st = re.sub(r"/\*(.|\n)*\*/", "",st);
st = re.sub(r"\n+", "\n",st);
sts = st.split('\n');

print(sts[2]);