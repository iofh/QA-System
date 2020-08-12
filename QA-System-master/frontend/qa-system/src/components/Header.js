import React from 'react';
import Typography from '@material-ui/core/Typography';


/**
 * Header components to be displayed first in web page,
 * with title and subtitle.
 */
class Header extends React.Component {
    render(){
        return(
        <div>
            <Typography align="center" component="h1" variant="h4">
                Experimental Q/A System
            </Typography>
            <Typography align="center" paragraph style = {{
            marginTop: 30,
            fontSize: 20,
            }}>
            The system is built to answer a user question by retrieving information from a specified domain.
            </Typography>
        </div>
        )
    }
}

export default Header