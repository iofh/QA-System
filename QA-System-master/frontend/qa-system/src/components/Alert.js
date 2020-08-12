import React from 'react'
import Alert from '@material-ui/lab/Alert'
import AlertTitle from '@material-ui/lab/AlertTitle'


/**
 * @param {*} props
 * Create Alert component, to show message to remind user.
 * props are passed to set message.
 */
function AlertComponent(props){
    return(
        <Alert severity="error" style={{
            fontSize: 16,
         }}>
          <AlertTitle>Error</AlertTitle>
            {props.message}
        </Alert>
    )
}

export default AlertComponent