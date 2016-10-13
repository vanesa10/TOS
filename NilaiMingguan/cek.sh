python data.py | awk -F " : " '{print $1}' > nrp.txt
readarray nrp < nrp.txt
rm nrp.txt
python data.py | awk -F " : " '{print $2}' > git.txt
readarray git < git.txt
rm git.txt
el=${#nrp[@]}
mkdir $1":"$2
cd $1":"$2
for (( i=0;i<el;i++)); do
  la=${#git[$i]}
  la=$la-1
  git[$i]=${git[$i]:0:$la}
  nrp[$i]=${nrp[$i]:0:8}
  echo https://github.com/${git[$i]}/${nrp[$i]}
  git clone https://github.com/${git[$i]}/${nrp[$i]}
  if [ -d ${nrp[$i]} ]; then
    cd ${nrp[$i]}
    jum=$(git log --pretty=format:"%ad" --since=$1 --until=$2 | grep -c ".*")
    cd ../
    nilai=0
    if [ $jum -gt 4 ];then
	nilai=100
    elif [ $jum -eq 4 ]; then
	nilai=85
    elif [ $jum -eq 3 ]; then
	nilai=75
    elif [ $jum -eq 2 ]; then
	nilai=68
    elif [ $jum -eq 1 ]; then
        nilai=60
    fi
    echo ${nrp[$i]}-$nilai
    echo ${nrp[$i]}-$nilai >> ../$1":"$2.txt
  fi
done
