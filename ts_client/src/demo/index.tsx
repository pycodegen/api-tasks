import * as React from 'react';
import * as ReactDOM from 'react-dom';
import {
  autobind,
} from 'core-decorators'


@autobind
export class InputView extends React.Component {
  onInput(event: React.ChangeEvent<HTMLInputElement>) {
    const file = event.target.files[0];
    console.log(1)
    debugger;
  }
  render() {
    return (
      <div>
      <input
        type="file"
        onChange={this.onInput}
      ></input>
      <p>aaa</p>
      </div>
    )
  }
}

ReactDOM.render(
  <InputView></InputView>,
  document.getElementById('root'),
)