import { Component, OnInit } from '@angular/core';
import { aboutusMockup } from '../../API';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.scss']
})
export class AboutComponent implements OnInit {
  aboutus = aboutusMockup;
  constructor() {}

  ngOnInit(): void {}
}
