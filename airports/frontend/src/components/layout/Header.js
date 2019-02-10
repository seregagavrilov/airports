import React, { Component } from 'react'

export class Header extends Component {
  render() {
    return (
        <nav class="navbar navbar-expand-sm navbar-light bg-light">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
          <a class="navbar-brand" href="#">Airports</a>
          <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
          </ul>
        </div>
        </nav>
    )
  }
}

export default Header
