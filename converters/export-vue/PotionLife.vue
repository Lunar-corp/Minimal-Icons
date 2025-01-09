<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    :stroke-width="stroke"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path d="m19,15h0c0,3.87-3.13,7-7,7h0c-3.87,0-7-3.13-7-7h0c0-3.18,2.11-5.85,5-6.71V2h4v6.29c1.13.33,2.14.95,2.95,1.76,1.27,1.27,2.05,3.01,2.05,4.95Z" /><line x1="16" y1="2" x2="14" y2="2" /><line x1="10" y1="2" x2="8" y2="2" /><path d="m15.4,15.43l-3.31,3.31-3.31-3.31c-.79-.79-.79-2.05,0-2.84s2.05-.79,2.84,0l.47.47.47-.47c.79-.79,2.05-.79,2.84,0s.79,2.05,0,2.84Z" />
  </svg>
</template>

<script setup>
  const props = defineProps({
    size: { type: [String, Number], default: 24 },
    stroke: { type: [String, Number], default: 1.5 },
  });
</script>

<style lang="scss" scoped></style>