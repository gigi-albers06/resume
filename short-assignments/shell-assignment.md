cd Destop
cd data
cd work
cd classes
cd GPGN268
cd coursework_albers
mkdir short-assignments
cd short-assignments
pwd
/Users/Gigi/Desktop/data/work/classes/GPGN268/coursework_albers/short-assignments

cd north-pacific-gyre
ls
mkdir NENE-A NENE-B
mv *A.txt* NENE-A
mv *B.txt* NENE-B
ls
cd NENE-A
wc -l *A.txt* | sort -nr
cd ..
cd NENE-B
wc -l *B.txt* | sort -nr

NENE02018B.txt has the least number of lines (240)

cd ..
rm *Z.txt*
ls


