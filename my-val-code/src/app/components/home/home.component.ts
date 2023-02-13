import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  left: number = 795;
  top: number = 59;

  noButtonStyles = {
    'color': 'black',
    'backgroundColor': 'red',
    'left': `${this.left}px`,
    'top': `${this.top}px`
  }


  constructor () {}

  ngOnInit(): void {}

  accepted(): void {
    alert(`Yeah! Thanks, See you soon!`);
  }

  rejected(): void {
    this.left = Math.floor(Math.random() * window.innerWidth);
    this.top = Math.floor(Math.random() * window.innerHeight);
  }
}
