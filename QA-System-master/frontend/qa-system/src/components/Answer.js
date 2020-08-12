import React from 'react';
import Typography from '@material-ui/core/Typography';


/**
 * @param {*} props
 * Create Answer component to show user entered question
 * and answer retrieved accordingly. props are passed to set data.
 */
function Answer(props) {
    return(
        <div>
            <Typography component="h1" variant="h5" style = {{
            marginTop: 30,
            }}>
              Question: {props.question}
            </Typography>
            <Typography component="h1" variant="h5" style = {{
            marginTop: 30,
            }}>
               Answer: {props.answer}
            </Typography>
        </div>
    )
}

export default Answer