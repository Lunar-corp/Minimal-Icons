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
    <path d="m17,15.3c.2-.4.5-.8.9-1,.85-.49,1.93-.33,2.6.4.3.4.5.8.5,1.3,0,1.3-2,2-2,2" /><path d="m19,20.98h.01" /><path d="m12,21h3" /><path d="m16.5,4.5c.83-.83,2.17-.83,3,0,.83.83.83,2.17,0,3l-12.5,12.5-4,1,1-4,12.5-12.5Z" />
  </svg>
</template>

<script setup>
  const props = defineProps({
    size: { type: [String, Number], default: 24 },
    stroke: { type: [String, Number], default: 1.5 },
  });
</script>

<style lang="scss" scoped></style>