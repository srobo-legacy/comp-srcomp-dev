echo 'Warning: This will reset all repos and checkout master.'
echo 'Press <return> to confirm.'
read

for repo in dummy-comp sr2014-comp sr2015-comp ranker srcomp srcomp-http srcomp-scorer srcomp-screens srcomp-stream srcomp-cli srcomp-kiosk; do
    echo $repo
    echo ------------------
    cd $repo
        git reset --hard HEAD
	git checkout master
    cd ..
    echo
done

echo srcomp-dev
echo ------------------
git reset --hard HEAD
git checkout master
