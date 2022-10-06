function display-title() {
    local title=$1
    echo
    echo '--------------------------------------------------------------------------------'
    echo "-- ${title}"
    echo '--------------------------------------------------------------------------------'
    echo
}

display-title 'Most correct guesses'

q "select url, artist, track, submitter, guesser from results.csv where submitter = guess order by submitter" \
    | q "select guesser, count(*) as correct from - group by guesser order by correct desc" \
    | tabulate-by-comma

display-title 'Most popular'

q "select submitter, artist, track, count(like) as likes from results.csv where like = 'X' group by url order by likes desc" \
    | tabulate-by-comma

display-title 'Most easily guessed'

q "select url, artist, track, submitter, guesser from results.csv where submitter = guess order by submitter" \
    | q "select submitter, count(*) as guessed_by from - group by submitter order by guessed_by desc" \
    | tabulate-by-comma

display-title 'Correctly guessed tracks'

q "select url, artist, track, submitter, guesser from results.csv where submitter = guess order by submitter" \
    | tabulate-by-comma


