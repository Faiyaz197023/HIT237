document.addEventListener('DOMContentLoaded', () => {
  // field refs
  const area     = document.getElementById('id_area_hectares');
  const rate     = document.getElementById('id_stocking_rate');
  const surveyed = document.getElementById('id_number_surveyed');
  const duration = document.getElementById('id_duration_minutes');
  const pest     = document.getElementById('id_pest_disease');

  // summary spans
  const sumEl      = document.getElementById('sum-plants');
  const pctEl      = document.getElementById('pct-inspected');
  const mppEl      = document.getElementById('min-per-plant');
  const reqSamples = document.getElementById('req-samples');
  const reqEffort  = document.getElementById('req-effort');

  // lookup: displayed option text ⇒ [sampling_rate, mins_per_sample]
  const pestConfig = {
    'Anthracnose':     { rate: 0.10, mins: 1.5 },
    'Dendritic Spot':  { rate: 0.05, mins: 1.0 },
    // add more pests here...
  };

  function recalc() {
    const a = parseFloat(area.value)   || 0;
    const r = parseFloat(rate.value)   || 0;
    const n = parseInt(surveyed.value) || 0;
    const d = parseInt(duration.value) || 0;

    // 1) expected total
    const total = Math.floor(a * r);
    sumEl.textContent = total > 0 ? total : '—';

    // 2) % inspected & actual min/plant
    if (total > 0 && n > 0) {
      pctEl.textContent = ((n / total) * 100).toFixed(1) + '%';
      mppEl.textContent = (d / n).toFixed(2) + ' min';
    } else {
      pctEl.textContent = '—';
      mppEl.textContent = '—';
    }

    // 3) derive pest key from selected option text
    const selOption = pest.options[pest.selectedIndex];
    const key = selOption ? selOption.text : '';
    const cfg = pestConfig[key] || { rate: 0, mins: 0 };

    // 4) recommended samples
    const neededSamples = Math.ceil(total * cfg.rate);
    reqSamples.textContent = neededSamples > 0 ? neededSamples : '—';

    // 5) estimated effort as percentage of total
    const effortPct = total > 0 ? (neededSamples / total) * 100 : 0;
    reqEffort.textContent = effortPct > 0 ? effortPct.toFixed(1) + '%' : '—';
  }

  // wire up both 'input' (for fields) and 'change' (for select)
  [area, rate, surveyed, duration].forEach(el => el.addEventListener('input', recalc));
  pest.addEventListener('change', recalc);

  // initial calculation
  recalc();
});
