import React from 'react';
import Box from '@material-ui/core/Box';
import Container from '@material-ui/core/Container';
import CssBaseline from '@material-ui/core/CssBaseline';
import Question from './components/Question'
import Header from './components/Header';
import Answer from './components/Answer';
import AlertComponent from './components/Alert'
import MenuItem from '@material-ui/core/MenuItem';
import CircularProgress from '@material-ui/core/CircularProgress';


/**
 * In the App class set state and handle event.
 * Then render compoments and pass state or event fucntion as
 * component props.
 */
class App extends React.Component {
  constructor() {
    super()
    this.state = {
      /** The selected domain to be shown. */
      domain: '',
      /** The question user entered. */
      question: "",
      /** The answer retrieved from backend. */
      answer: "",
      /** Domain list retrieved from db. */
      domainList:[],
      /** Flag to check whether Check Button is clicked. */
      formSubmit: false,
      /** Flag to check whether retrieving answer is ongoing. */
      loading: false,
      /** Flag to check whether any error message to show. */
      withMsg: false,
      /** message to remind user. */
      message: ""
    }
    this.handleChange =  this.handleChange.bind(this)
    this.handleSubmit =  this.handleSubmit.bind(this)
  }

  /**
  * Fetch domain according to API,
  * then set data to state.
  */
  componentDidMount() {
    let getDomainUrl = 'http://10.118.0.158:8080/domain'
        fetch(getDomainUrl)
            .then(response => response.json())
            .then((data) => {
                this.setState({
                    domainList: data,
                    domain: data[0]
                })
            })
  }

  /**
   * @param {*} event
   * Reset answer state if it has value or
   * set input box value of question to state or
   * set selected value of domain to state.
   */
  handleChange(event) {
      const {name, value} = event.target
      if(this.state.answer !== "") {
        this.setState({ answer: "" })
      }
      this.setState({
        [name]: value
      })
  }

  /**
   * @param {*} e
   * Pass parameter domain and question then fetch answer
   * according to API, and set state accordingly if question
   * is not empty, otherwise show message to reminder user enter
   * question.
   */
  handleSubmit(e) {
    e.preventDefault();
    let query_domain = this.state.domain;
    let query_question = this.state.question;
    if(query_question) {
      this.setState({
        formSubmit: true,
        loading: true,
        withMsg: false
      });

      fetch('http://10.118.0.158:8080/answer?domain=' + query_domain + '&question=' + query_question,
      {
        method: 'GET',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'applciation/json'
      }
      })
      .then(res => res.json())
      .then(res => {
            this.setState({
              loading: false,
              answer: res['answer']
            });
        })
      .catch(err => console.log(err))
    }
    else {
      this.setState({
        withMsg: true,
        message: "Please enter your question."
      });
    }
  }

  /**
   * Render components and pass state or parameters to
   * each compoment as its props.
   */
  render(){
    let gotAnswer = this.state.answer;

    const renderAnswer = ()=>{
      if(gotAnswer){
        /**
         * Show Answer component only when answer is retrieved.
         */
        return <Answer
          question={this.state.question}
          answer={this.state.answer}
        />
      }
      else if(this.state.formSubmit && this.state.loading){
        /**
         * If answer retrieving is not finished,
         * spinner will show to remind user.
         */
        return(
        <div style={{
          marginTop: 50,
          position: 'absolute',
          left: '49%',
      }}>
        <CircularProgress thickness={3.9} size = {50}/>
       </div>
       )
      }
    }

    /**
     * Map domain list to select options.
     */
    const options = this.state.domainList.map((domainValue,index) =>
          <MenuItem key={index} value={domainValue}>{domainValue}</MenuItem>
        )

  return (
    <div style={{
      marginTop: 30,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
    }}>
      <Container component="main" maxWidth="sm">
        <Box>
        <CssBaseline />
          <Header></Header>
          {
            this.state.withMsg &&
            <AlertComponent message={this.state.message}/>
          }
          <Question
            handleChange={this.handleChange}
            handleSubmit={this.handleSubmit}
            handleSelectChange={this.handleSelectChange}
            domain={this.state.domain}
            question={this.state.question}
            options={options}
            {...this.state}
          />
          {renderAnswer()}
        </Box>
      </Container>
    </div>
  )
}}

export default App;
