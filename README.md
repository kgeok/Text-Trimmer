# Text-Trimmer

Utility for isolating lines of text right from the command line onto a new file

```console
foo@bar:~$ py TextTrimmer.py -t <FileName.txt> <Beginning Text> <End Text>
```

Example:

Input:

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Rhoncus mattis rhoncus urna neque viverra justo. Lectus magna fringilla urna porttitor. Non odio euismod lacinia at quis. Dolor magna eget est lorem ipsum. In est ante in nibh mauris cursus mattis. Etiam sit amet nisl purus in mollis. Leo duis ut diam quam nulla. Aliquam faucibus purus in massa tempor nec feugiat nisl pretium. Dui vivamus arcu felis bibendum ut tristique et. Nec ultrices dui sapien eget mi proin. Imperdiet dui accumsan sit amet nulla facilisi. Id eu nisl nunc mi ipsum faucibus. Posuere ac ut consequat semper. Ornare suspendisse sed nisi lacus sed. Cursus sit amet dictum sit amet justo. Suscipit adipiscing bibendum est ultricies. Elementum integer enim neque volutpat ac tincidunt. Urna porttitor rhoncus dolor purus non enim praesent. Iaculis eu non diam phasellus vestibulum lorem sed risus ultricies. Interdum varius sit amet mattis vulputate enim nulla aliquet. Aliquam faucibus purus in massa tempor nec feugiat nisl pretium. Tortor at auctor urna nunc. Dolor morbi non arcu risus quis. Aliquam malesuada bibendum arcu vitae. Urna et pharetra pharetra massa massa ultricies mi. Eget gravida cum sociis natoque penatibus et magnis.

```console
foo@bar:~$ py TextTrimmer.py -t <FileName.txt> Non ultricies
```

Output: 

Non odio euismod lacinia at quis. Dolor magna eget est lorem ipsum. In est ante in nibh mauris cursus mattis. Etiam sit amet nisl purus in mollis. Leo duis ut diam quam nulla. Aliquam faucibus purus in massa tempor nec feugiat nisl pretium. Dui vivamus arcu felis bibendum ut tristique et. Nec ultrices dui sapien eget mi proin. Imperdiet dui accumsan sit amet nulla facilisi. Id eu nisl nunc mi ipsum faucibus. Posuere ac ut consequat semper. Ornare suspendisse sed nisi lacus sed. Cursus sit amet dictum sit amet justo. Suscipit adipiscing bibendum est ultricies.
