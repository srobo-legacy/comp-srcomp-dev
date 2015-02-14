for repo in dummy-comp ranker srcomp srcomp-http srcomp-scorer srcomp-screens srcomp-stream; do
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
