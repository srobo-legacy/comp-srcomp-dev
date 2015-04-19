for repo in dummy-comp sr2014-comp sr2015-comp ranker srcomp srcomp-http srcomp-scorer srcomp-screens srcomp-stream srcomp-cli srcomp-kiosk; do
    echo $repo
    echo ------------------
    cd $repo
        git pull --ff-only
    cd ..
    echo
done

echo srcomp-dev
echo ------------------
git pull --ff-only
