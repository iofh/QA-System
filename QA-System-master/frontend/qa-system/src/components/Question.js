import React from 'react';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';
import InputLabel from '@material-ui/core/InputLabel';
import Select from '@material-ui/core/Select';


/**
 * @param {*} props
 * Create Question component, including Domain select options,
 * Question input box and Check Answer button.
 * props are passed to handle event or set data.
 */
function Question(props){
  return (
    <div>
        <form noValidate onSubmit={props.handleSubmit} style={{
           width: '100%',
           marginTop: 3,
        }}>
        <Grid container spacing={5}>
          <Grid item xs={12} >
          <InputLabel id="label" color='primary' style={{
           marginTop: 30,
           fontSize: 20
        }}>
          Please choose your domain
        </InputLabel>
        <Select
          labelId="domain"
          value={props.domain}
          name="domain"
          fullWidth
          label="Please choose your domain"
          onChange={props.handleChange}
          required
          style={{
            marginTop: 15,
         }}>
              {props.options}
        </Select>
          </Grid>
            <Grid item xs={8}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="question"
                label="Your Question"
                onChange={props.handleChange}
                autoFocus
              />
            </Grid>
            <Grid item xs={4}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="voice"
                label="voiceicon"
                name="voice"
              />
            </Grid>
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            style={{
              marginTop:30
            }}
          >
            Check Answer
          </Button>
        </form>
      </div>
  )
}

export default Question