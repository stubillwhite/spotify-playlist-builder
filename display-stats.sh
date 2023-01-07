#!/bin/bash

function display-title() {
    local title=$1
    echo
    echo '--------------------------------------------------------------------------------'
    echo "-- ${title}"
    echo '--------------------------------------------------------------------------------'
    echo
}

#CSV_FILENAME=recs-summer-playlist-quiz-master.csv
CSV_FILENAME=recs-roadtrip-playlist-quiz-master.csv

display-title 'Most correct guesses'

CMD='q --delimiter=, --skip-header --output-header'

${CMD} "select url, artist, track, submitter, guesser from ${CSV_FILENAME} where submitter = guess order by submitter" \
    | ${CMD} "select guesser, count(*) as correct from - group by guesser order by correct desc" \
    | gsed 's/,,/,-,/g' \
    | column -t -s '',''

display-title 'Most popular'

${CMD} "select submitter, artist, track, count(like) as likes from ${CSV_FILENAME} where like = 'X' group by url order by likes desc" \
    | gsed 's/,,/,-,/g' \
    | column -t -s '',''

display-title 'Most easily guessed'

${CMD} "select url, artist, track, submitter, guesser from ${CSV_FILENAME} where submitter = guess order by submitter" \
    | ${CMD} "select submitter, count(*) as guessed_by from - group by submitter order by guessed_by desc" \
    | gsed 's/,,/,-,/g' \
    | column -t -s '',''

display-title 'Correctly guessed tracks'

${CMD} "select url, artist, track, submitter, guesser from ${CSV_FILENAME} where submitter = guess order by submitter" \
    | gsed 's/,,/,-,/g' \
    | column -t -s '',''
