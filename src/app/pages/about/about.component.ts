import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { aboutusMockup } from '../../API';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.scss']
})
export class AboutComponent implements OnInit {
  aboutus = aboutusMockup;
  sectionTitle: any;
  constructor(private route: ActivatedRoute, private location: Location) {}

  ngOnInit() {}
}
