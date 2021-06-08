import { Component, OnInit } from '@angular/core';
import { servicesMockup } from '../../API';

@Component({
  selector: 'app-services',
  templateUrl: './services.component.html',
  styleUrls: ['./services.component.scss']
})
export class ServicesComponent implements OnInit {
  services = servicesMockup;

  constructor() {}

  ngOnInit(): void {}
}
