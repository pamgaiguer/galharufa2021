import { Component, OnInit } from '@angular/core';
import { activitiesMockup } from '../../API';

@Component({
  selector: 'app-activities',
  templateUrl: './activities.component.html',
  styleUrls: ['./activities.component.scss']
})
export class ActivitiesComponent implements OnInit {
  activities = activitiesMockup;
  active = 'interp';

  constructor() {}

  ngOnInit(): void {}
}
